"""Non-destructive URL/text checking, not a vendor pricing scraper."""
import argparse,html,json,re,time
from datetime import datetime,timezone
from pathlib import Path
from urllib.error import HTTPError,URLError
from urllib.request import Request,urlopen
from catalog import ROOT,read_json
def check_sources(config):
    findings=[]
    for item in config['watches']:
        outcome={'name':item['name'],'url':item['url'],'state':'unavailable','details':''}
        try:
            req=Request(item['url'],headers={'User-Agent':'llm-api-pricing-tracker/1.0'})
            with urlopen(req,timeout=15) as response:page=response.read(2_000_000).decode('utf-8',errors='replace')
            readable=re.sub(r'\s+',' ',html.unescape(re.sub(r'(?is)<[^>]+>',' ',page)))
            if all(re.search(p,readable,re.IGNORECASE) for p in item.get('patterns',[])):
                outcome['state']='found';outcome['details']='Configured terms found; rates are NOT guaranteed unchanged.'
            else:
                outcome['state']='needs_review';outcome['details']='Term absent; review for dynamic HTML or pricing changes.'
        except (HTTPError,URLError,TimeoutError,ValueError) as e:
            outcome['details']=f'{type(e).__name__}: {str(e)[:130]}'
        findings.append(outcome);time.sleep(.1)
    return {'checked_at_utc':datetime.now(timezone.utc).isoformat(),'results':findings}
def main():
    parser=argparse.ArgumentParser();parser.add_argument('--out',default='source-report.json');parser.add_argument('--strict',action='store_true')
    args=parser.parse_args();report=check_sources(read_json(ROOT/'data/source-watches.json'))
    Path(args.out).write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    for item in report['results']:print(item['state'],item['name'],item['details'])
    return int(args.strict and any(item['state']=='needs_review' for item in report['results']))
if __name__=='__main__':raise SystemExit(main())
