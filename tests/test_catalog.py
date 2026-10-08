import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from catalog import catalog, validate, combined, sorted_rates, access_display, params_display
from generate_readme import make_table, money

class CatalogTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.models,cls.rates=catalog()

    def test_data_validates(self):
        self.assertEqual(validate(self.models,self.rates),[])

    def test_price_arithmetic(self):
        self.assertAlmostEqual(combined({'input':0.10,'output':0.50}),0.60)

    def test_sorted_cost_non_decreasing(self):
        r=sorted_rates(self.rates)
        self.assertEqual([round(combined(x),7) for x in r],
                         sorted(round(combined(x),7) for x in r))

    def test_cache_tiebreaker(self):
        r=sorted_rates([{'input':2,'output':10,'cached_input':.2,'label':'A'},
                        {'input':2,'output':10,'cached_input':.1,'label':'B'}])
        self.assertEqual(r[0]['label'],'B')

    def test_parameter_render(self):
        mid=next(k for k,v in self.models.items() if v['name']=='Mistral Small 4')
        self.assertIn('119B',params_display([mid],self.models))
        self.assertIn('6.5B active',params_display([mid],self.models))

    def test_contributor_not_merged_with_standard(self):
        names=[r['label'] for r in self.rates]
        self.assertTrue(any('Contributor' in n for n in names))
        self.assertTrue(any('Muse Spark 1.1/1.2/1.3' == n for n in names))

    def test_open_closed_are_only_labels(self):
        self.assertEqual({m['openness'] for m in self.models.values()}, {'Open','Closed'})
        self.assertTrue(all('weights_status' not in m for m in self.models.values()))
        self.assertEqual(access_display(['qwen--qwen3-8-max'], self.models), 'Open')
        self.assertEqual(access_display(['qwen--qwen3-7-flash'], self.models), 'Closed')

    def test_currency_display_never_has_float_artifacts(self):
        self.assertEqual(money(0.1+0.2),'$0.30')
        self.assertEqual(money(0.3+1.1),'$1.40')
        self.assertEqual(money(0.003),'$0.003')
        self.assertEqual(money(0.125),'$0.125')
        self.assertEqual(money(2.0),'$2.00')
        table=make_table()
        self.assertNotIn('$0.300000',table)
        self.assertNotIn('$1.400000',table)
        self.assertNotIn('Open weights',table)

    def test_deepseek_new_flash_params_not_old_flash(self):
        ds=self.models['deepseek--deepseek-v4-1-flash']
        self.assertEqual(ds['total_parameters_b'],552)
        self.assertEqual(ds['active_parameters_range_b'],[8,16])
        self.assertIn('8B–16B active',params_display([ds['id']],self.models))

    def test_kimi_open_models_and_speed_tier(self):
        ids = [
            'kimi--kimi-k2-6', 'kimi--kimi-k2-7-code',
            'kimi--kimi-k2-7-code-highspeed', 'kimi--kimi-k3'
        ]
        self.assertTrue(all(self.models[mid]['openness'] == 'Open' for mid in ids))
        self.assertEqual(self.models['kimi--kimi-k2-6']['total_parameters_b'], 1000)
        self.assertEqual(self.models['kimi--kimi-k2-7-code']['active_parameters_b'], 32)
        highspeed = self.models['kimi--kimi-k2-7-code-highspeed']
        self.assertEqual(highspeed['active_parameters_b'], 32)
        self.assertEqual(highspeed['hosted_variant_of'], 'kimi--kimi-k2-7-code')

    def test_glm_turbo_not_assumed_open(self):
        turbo = self.models['glm-z-ai--glm-5-turbo']
        self.assertEqual(turbo['openness'], 'Closed')
        self.assertIsNone(turbo['total_parameters_b'])
        self.assertEqual(self.models['glm-z-ai--glm-5']['openness'], 'Open')

    def test_readme_has_visible_update_date(self):
        readme = (Path(__file__).resolve().parents[1] / 'README.md').read_text(encoding='utf-8')
        self.assertIn('## Last updated: **2026-10-08**', readme.split('<!-- CATALOG:START -->')[0])
        self.assertIn('| Kimi | Kimi K2.7 Code Highspeed | Open |', readme)

    def test_table_row_count(self):
        table=make_table()
        self.assertEqual(len(table.splitlines()),len(self.rates)+2)

if __name__=='__main__':
    unittest.main()
