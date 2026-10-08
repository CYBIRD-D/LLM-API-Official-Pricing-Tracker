"""Create the individual-model parameter and weight catalog."""
from catalog import ROOT,catalog,validate
def esc(s):return str(s).replace('|','\\|').replace('\n',' ')
def make_model_catalog():
    models,rates=catalog();errors=validate(models,rates)
    if errors:raise ValueError('; '.join(errors))
    lines=['# Model Weights, Licenses and Parameters','',
      'Generated from [`data/models.json`](../data/models.json). Unknown values are deliberately not guessed.',
      '', '| Provider | Model | Availability of weights | License | Parameters (total / active) | Architecture | Model card |',
      '|---|---|---|---|---|---|---|']
    for m in sorted(models.values(),key=lambda x:(x['provider'].lower(),x['name'].lower())):
        v=m['weights_status'].replace('_',' ');t=m['total_parameters_b'];a=m['active_parameters_b']
        param='Unknown' if t is None else f'{t:g}B'+(f' / {a:g}B active' if a is not None else '')
        link='[Model card]('+m['parameter_source']+')' if m['parameter_source'] else '—'
        vals=[m['provider'],m['name'],v,m['license'] or 'Not verified',param,m['architecture'] or 'Not disclosed',link]
        lines.append('| '+' | '.join(esc(x) for x in vals)+' |')
    lines+=['','**Note:** `announced_open_weight` means the release is planned, not that weights are downloadable. Data about model parameters is held to the standards in [methodology](methodology.md).','']
    return '\n'.join(lines)
if __name__=='__main__':
    (ROOT/'docs/model-catalog.md').write_text(make_model_catalog(),encoding='utf8')
    print('Regenerated docs/model-catalog.md')
