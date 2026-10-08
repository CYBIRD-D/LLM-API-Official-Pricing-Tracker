"""Shared data access and validation for the LLM pricing catalog (stdlib only)."""
from __future__ import annotations
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODELS = ROOT / 'data/models.json'
PRICING = ROOT / 'data/pricing.json'
VALID_OPENNESS = {'Open', 'Closed'}
VALID_RATE_TYPES = {'standard', 'promo', 'regular', 'peak', 'off_peak', 'contributor', 'highspeed'}


def read_json(path: Path) -> dict:
    with path.open(encoding='utf-8') as f:
        return json.load(f)


def catalog() -> tuple[dict[str, dict], list[dict]]:
    return ({m['id']: m for m in read_json(MODELS)['models']},
            read_json(PRICING)['prices'])


def combined(rate: dict) -> float:
    return rate['input'] + rate['output']


def sorted_rates(rates: list[dict]) -> list[dict]:
    # A missing cache price is unknown, never interpreted as $0.
    return sorted(rates, key=lambda r: (round(combined(r), 7),
                        math.inf if r['cached_input'] is None else r['cached_input'],
                        r['input'], r['label'].lower()))


def validate(models: dict[str, dict], rates: list[dict]) -> list[str]:
    errors = []
    seen = set()
    for ident, model in models.items():
        if model.get('id') != ident:
            errors.append(f'{ident}: mismatched model ID')
        if model.get('openness') not in VALID_OPENNESS:
            errors.append(f'{ident}: invalid openness (must be Open or Closed)')
        for fld in ('total_parameters_b', 'active_parameters_b'):
            p = model.get(fld)
            if p is not None and (not isinstance(p, (int, float)) or p <= 0):
                errors.append(f'{ident}: invalid {fld}')
        a, t = model.get('active_parameters_b'), model.get('total_parameters_b')
        span = model.get('active_parameters_range_b')
        if span is not None and (not isinstance(span, list) or len(span) != 2
            or not all(isinstance(v, (int, float)) and v > 0 for v in span)
            or span[0] > span[1] or (t is not None and span[1] > t)):
            errors.append(f'{ident}: invalid active parameters range')
        if a is not None and t is not None and a > t:
            errors.append(f'{ident}: active parameters exceed total parameters')
        if (a is not None or t is not None or span is not None) and not model.get('parameter_source'):
            errors.append(f'{ident}: parameter count needs a source')
    for rate in rates:
        rid = rate.get('id')
        if not rid or rid in seen:
            errors.append(f'duplicate/missing rate ID: {rid}')
        seen.add(rid)
        if not rate.get('model_ids'):
            errors.append(f'{rid}: no models')
        for mid in rate.get('model_ids', []):
            if mid not in models:
                errors.append(f'{rid}: missing model {mid}')
        for col in ('input', 'output', 'cached_input'):
            v = rate.get(col)
            if col != 'cached_input' or v is not None:
                if isinstance(v, bool) or not isinstance(v, (int,float)) or not math.isfinite(v) or v < 0:
                    errors.append(f'{rid}: invalid {col}')
        if rate.get('rate_type') not in VALID_RATE_TYPES:
            errors.append(f'{rid}: invalid rate type')
        if not str(rate.get('pricing_source', '')).startswith('https://'):
            errors.append(f'{rid}: source URL missing/invalid')
    return errors


def access_display(ids: list[str], models: dict[str, dict]) -> str:
    labels={models[mid]['openness'] for mid in ids}
    return next(iter(labels)) if len(labels)==1 else 'Mixed'


def params_display(ids: list[str], models: dict[str, dict]) -> str:
    def one(m):
        total=m['total_parameters_b']
        active=m['active_parameters_b']
        span=m.get('active_parameters_range_b')
        if total is None:
            return 'Not disclosed'
        def size(v):
            if v >= 1000:
                x=v / 1000
                return f'{x:g}T'
            return f'{v:g}B'
        prefix = '≈' if m.get('parameter_basis') == 'founder_claim' else ''
        text=prefix + size(total)
        if active is not None:
            text+=' / '+size(active)+' active'
        elif span:
            text+=' / '+size(span[0])+'–'+size(span[1])+' active'
        if m.get('parameter_basis')=='founder_claim':
            text+=' (Musk claim)'
        return text
    distinct={one(models[mid]) for mid in ids}
    return next(iter(distinct)) if len(distinct)==1 else 'Varies / see catalog'
