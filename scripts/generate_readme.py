"""Regenerate the README's Markdown leaderboard from data/*.json."""
from pathlib import Path
from catalog import ROOT, catalog, validate, sorted_rates, access_display, params_display, combined

START='<!-- CATALOG:START -->'
END='<!-- CATALOG:END -->'

def money(value):
    """Human-readable USD without binary-float artifacts or redundant zeroes."""
    if value is None:
        return '—'
    numeric = f'{round(float(value), 6):.6f}'.rstrip('0').rstrip('.')
    if '.' not in numeric:
        numeric += '.00'
    elif len(numeric.partition('.')[2]) == 1:
        numeric += '0'
    return '$' + numeric

def escape(s):
    return str(s).replace('|', '\\|').replace('\n', ' ').replace('\r',' ')

def make_table():
    models, rates = catalog()
    problems = validate(models, rates)
    if problems:
        raise ValueError('Catalog validation failed: '+'; '.join(problems))
    head=['Rank','Provider','Model','Open/Closed','Parameters (Total / Active)',
          'Input','Cached Input','Output','Combined','Notes','Pricing source']
    lines=['| '+' | '.join(head)+' |','|'+'|'.join(['---:']+['---']*4+['---:']*4+['---']*2)+'|']
    for idx,rate in enumerate(sorted_rates(rates),1):
        mids=rate['model_ids']
        source=f"[Source]({rate['pricing_source']})"
        name=rate['label']
        param_text=params_display(mids,models)
        parameter_sources={models[mid].get('parameter_source') for mid in mids}
        if param_text != 'Not disclosed' and len(parameter_sources)==1 and None not in parameter_sources:
            param_text=f"[{param_text}]({next(iter(parameter_sources))})"
        data=[str(idx), rate['model_ids'] and models[mids[0]]['provider'],
              name, access_display(mids,models),param_text,
              money(rate['input']),money(rate['cached_input']),money(rate['output']),
              '**'+money(combined(rate))+'**',rate.get('notes','') or '—',source]
        lines.append('| '+' | '.join(escape(x) for x in data)+' |')
    return '\n'.join(lines)

def regenerate(readme=None):
    readme=Path(readme) if readme else ROOT/'README.md'
    text=readme.read_text(encoding='utf-8')
    if text.count(START)!=1 or text.count(END)!=1:
        raise ValueError('README needs exactly one pair of CATALOG markers')
    before, rest=text.split(START)
    _,after=rest.split(END)
    updated=before+START+'\n'+make_table()+'\n'+END+after
    readme.write_text(updated,encoding='utf-8')
    return updated

if __name__=='__main__':
    regenerate()
    print('Regenerated README.md')
