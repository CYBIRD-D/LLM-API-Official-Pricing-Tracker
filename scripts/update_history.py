"""Record locally edited rates without inventing vendor announcement dates."""
import json
from datetime import datetime,timezone
from catalog import ROOT,read_json,PRICING
BASE=ROOT/'data/last-recorded-prices.json';HIST=ROOT/'data/pricing-history.json'
FIELDS=['input','cached_input','output','rate_type','notes','pricing_source']
def main():
    now=datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00','Z')
    current={r['id']:{k:r.get(k) for k in FIELDS} for r in read_json(PRICING)['prices']}
    previous=read_json(BASE)['prices'] if BASE.exists() else {}
    history=read_json(HIST);events=[]
    for ident in sorted(set(previous)|set(current)):
        old=previous.get(ident);new=current.get(ident)
        if old!=new:events.append({'recorded_at_utc':now,'price_id':ident,'old':old,'new':new,'note':'Local catalog change only; not a vendor announcement date.'})
    history['events'].extend(events)
    HIST.write_text(json.dumps(history,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    BASE.write_text(json.dumps({'schema_version':1,'prices':current},indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    print(f'Recorded {len(events)} local changes.')
if __name__=='__main__':main()
