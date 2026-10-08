"""Create the individual-model Open/Closed and parameter index."""
from catalog import ROOT,catalog,validate,params_display

def esc(s):
    return str(s).replace('|','\\|').replace('\n',' ')

def make_model_catalog():
    models,rates=catalog()
    errors=validate(models,rates)
    if errors: raise ValueError('; '.join(errors))
    lines=['# Model Openness, Licenses and Parameters','',
      'Generated from [`data/models.json`](../data/models.json). **Open** = matching downloadable model checkpoint; **Closed** = no matching public checkpoint verified. These labels do not indicate whether a license is OSI-approved.',
      '', '| Provider | Model | Open/Closed | License | Parameters (total / active) | Architecture | Evidence | Notes |',
      '|---|---|---|---|---|---|---|---|']
    for m in sorted(models.values(),key=lambda x:(x['provider'].lower(),x['name'].lower())):
        param=params_display([m['id']],models)
        link='[Source]('+m['parameter_source']+')' if m.get('parameter_source') else '—'
        notes='; '.join(filter(None,[m.get('parameter_notes'),m.get('openness_note')])) or '—'
        vals=[m['provider'],m['name'],m['openness'],m.get('license') or 'Not verified',param,m.get('architecture') or 'Not disclosed',link,notes]
        lines.append('| '+' | '.join(esc(x) for x in vals)+' |')
    lines += ['','**Caution:** A branded hosted API may have extra tools/context or post-training changes relative to a corresponding released checkpoint. Founder-claimed figures are not independently verified. See [methodology](methodology.md).','']
    return '\n'.join(lines)

if __name__=='__main__':
    path=ROOT/'docs/model-catalog.md'
    path.write_text(make_model_catalog(),encoding='utf8')
    print('Regenerated docs/model-catalog.md')
