"""Regenerate the README leaderboard from structured JSON."""
from pathlib import Path
from catalog import ROOT,catalog,validate,sorted_rates,access_display,params_display,combined
START='<!-- CATALOG:START -->';END='<!-- CATALOG:END -->'
def money(value):
    if value is None:return '—'
    places=next((n for n in (2,3,4,5) if round(value,n)==value),6)
    return '$'+f'{value:.{places}f}'
def escape(s):
    return str(s).replace('|','\\|').replace('\n',' ').replace('\r',' ')
def make_table():
    models,rates=catalog();problems=validate(models,rates)
    if problems:raise ValueError('; '.join(problems))
    head=['Rank','Provider','Model','Weights','Parameters (Total / Active)','Input','Cached Input','Output','Combined','Notes','Pricing source']
    lines=['| '+' | '.join(head)+' |','|'+'|'.join(['---:']+['---']*4+['---:']*4+['---']*2)+'|']
    for idx,rate in enumerate(sorted_rates(rates),1):
        mids=rate['model_ids'];param_text=params_display(mids,models)
        param_sources={models[mid].get('parameter_source') for mid in mids}
        if param_text!='Not disclosed' and len(param_sources)==1 and None not in param_sources:
            param_text=f"[{param_text}]({next(iter(param_sources))})"
        data=[str(idx),models[mids[0]]['provider'],rate['label'],access_display(mids,models),param_text,money(rate['input']),money(rate['cached_input']),money(rate['output']),'**'+money(combined(rate))+'**',rate.get('notes','') or '—',f"[Source]({rate['pricing_source']})"]
        lines.append('| '+' | '.join(escape(x) for x in data)+' |')
    return '\n'.join(lines)
def regenerate(readme=None):
    readme=Path(readme) if readme else ROOT/'README.md'
    text=readme.read_text(encoding='utf-8')
    if text.count(START)!=1 or text.count(END)!=1:raise ValueError('Missing README markers')
    before,rest=text.split(START);_,after=rest.split(END)
    updated=before+START+'\n'+make_table()+'\n'+END+after
    readme.write_text(updated,encoding='utf-8')
    return updated
if __name__=='__main__':
    regenerate();print('Regenerated README.md')
