import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from catalog import catalog,validate,combined,sorted_rates,params_display
from generate_readme import make_table
class CatalogTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.models,cls.rates=catalog()
    def test_data_validates(self):self.assertEqual(validate(self.models,self.rates),[])
    def test_price_arithmetic(self):self.assertAlmostEqual(combined({'input':.1,'output':.5}),.6)
    def test_sorted_cost_non_decreasing(self):
        s=sorted_rates(self.rates);self.assertEqual([round(combined(x),7) for x in s],sorted(round(combined(x),7) for x in s))
    def test_cache_tiebreaker(self):
        s=sorted_rates([{'input':2,'output':10,'cached_input':.2,'label':'A'},{'input':2,'output':10,'cached_input':.1,'label':'B'}]);self.assertEqual(s[0]['label'],'B')
    def test_parameter_render(self):
        mid=next(k for k,v in self.models.items() if v['name']=='Mistral Small 4')
        self.assertIn('119B',params_display([mid],self.models))
        self.assertIn('6.5B active',params_display([mid],self.models))
    def test_contributor_not_merged_with_standard(self):
        names=[r['label'] for r in self.rates]
        self.assertTrue(any('Contributor' in n for n in names))
        self.assertTrue(any('Muse Spark 1.1/1.2/1.3'==n for n in names))
    def test_table_row_count(self):self.assertEqual(len(make_table().splitlines()),len(self.rates)+2)
if __name__=='__main__':unittest.main()
