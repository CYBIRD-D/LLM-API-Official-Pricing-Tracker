"""Shared catalog access, deterministic sorting and validation."""
import json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
MODELS=ROOT/'data/models.json'; PRICING=ROOT/'data/pricing.json'
VALID_WEIGHT_STATUSES={'open_weight','closed_weight','announced_open_weight','unknown'}
VALID_RATE_TYPES={'standard','promo','regular','peak','off_peak','contributor','highspeed'}
def read_json(path):
    return json.loads(path.read_text(encoding='utf-8'))
def catalog():
    return ({m['id']:m for m in read_json(MODELS)['models']},read_json(PRICING)['prices'])
def combined(rate):return rate['input']+rate['output']
def sorted_rates(rates):
    return sorted(rates,key=lambda r:(round(combined(r),7),math.inf if r['cached_input'] is None else r['cached_input'],r['input'],r['label'].lower()))
def validate(models,rates):
    errors=[];seen=set()
    for ident,m in models.items():
        if m.get('id')!=ident:errors.append(f'{ident}: mismatched model ID')
        if m.get('weights_status') not in VALID_WEIGHT_STATUSES:errors.append(f'{ident}: invalid weights status')
        for fld in ('total_parameters_b','active_parameters_b'):
            p=m.get(fld)
            if p is not None and (not isinstance(p,(int,float)) or p<=0):errors.append(f'{ident}: invalid {fld}')
        a,t=m.get('active_parameters_b'),m.get('total_parameters_b')
        if a is not None and t is not None and a>t:errors.append(f'{ident}: active exceeds total')
        if (a is not None or t is not None) and not m.get('parameter_source'):errors.append(f'{ident}: missing parameter source')
    for r in rates:
        rid=r.get('id')
        if not rid or rid in seen:errors.append(f'duplicate/missing rate ID: {rid}')
        seen.add(rid)
        if not r.get('model_ids'):errors.append(f'{rid}: no models')
        for mid in r.get('model_ids',[]):
            if mid not in models:errors.append(f'{rid}: missing model {mid}')
        for col in ('input','output','cached_input'):
            v=r.get(col)
            if col!='cached_input' or v is not None:
                if isinstance(v,bool) or not isinstance(v,(int,float)) or not math.isfinite(v) or v<0:errors.append(f'{rid}: invalid {col}')
        if r.get('rate_type') not in VALID_RATE_TYPES:errors.append(f'{rid}: invalid rate type')
        if not str(r.get('pricing_source','')).startswith('https://'):errors.append(f'{rid}: invalid pricing source')
    return errors
def access_display(ids,models):
    statuses={models[mid]['weights_status'] for mid in ids}
    d={'open_weight':'Open weights','closed_weight':'Closed weights','announced_open_weight':'Announced, not released','unknown':'Unverified'}
    return d[next(iter(statuses))] if len(statuses)==1 else 'Mixed / see catalog'
def params_display(ids,models):
    pairs={(models[mid]['total_parameters_b'],models[mid]['active_parameters_b']) for mid in ids}
    if len(pairs)!=1:return 'Varies / see catalog'
    total,active=next(iter(pairs))
    if total is None:return 'Not disclosed'
    fmt=lambda n:(f'{n:,.0f}' if n==int(n) else f'{n:,.1f}')+'B'
    return fmt(total)+(' / '+fmt(active)+' active' if active is not None else '')
