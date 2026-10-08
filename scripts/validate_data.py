"""Validate JSON catalog consistency."""
import sys
from catalog import catalog,validate
if __name__=='__main__':
    m,r=catalog();problems=validate(m,r)
    for p in problems:print('ERROR:',p,file=sys.stderr)
    if not problems:print(f'PASS: {len(m)} models, {len(r)} price entries.')
    sys.exit(bool(problems))
