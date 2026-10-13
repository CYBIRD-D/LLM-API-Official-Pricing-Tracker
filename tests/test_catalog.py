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
        self.assertIn('## Last updated: **2026-10-14**', readme.split('<!-- CATALOG:START -->')[0])
        self.assertIn('| Kimi | Kimi K2.7 Code Highspeed | Open |', readme)

    def test_new_models_and_deprecation(self):
        rows = {r['id']: r for r in self.rates}
        self.assertEqual(self.models['google--gemini-4-argon']['openness'], 'Closed')
        self.assertEqual(self.models['meta--muse-wonder-1-0']['openness'], 'Closed')
        self.assertEqual(self.models['meta--muse-wonder-full-1-0']['api_status'], 'subscription_only')
        self.assertNotIn('meta--muse-wonder-full-1-0', [mid for r in self.rates for mid in r['model_ids']])
        self.assertEqual(rows['google--gemini-4-argon-promo']['input'], 2.0)
        self.assertEqual(rows['google--gemini-4-argon-promo']['output'], 10.0)
        self.assertEqual(rows['google--gemini-4-argon-promo']['promo_ends_on'], '2026-11-30')
        self.assertEqual(rows['google--gemini-4-argon-regular']['effective_from'], '2026-12-01')
        self.assertEqual(rows['meta--muse-wonder-1-0']['cached_input'], 0.20)
        self.assertNotIn('google--gemini-3-5-flash', rows)
        self.assertEqual(self.models['google--gemini-3-7-flash']['redirects_to'], 'gemini-3.8-flash')
        self.assertEqual(self.models['google--gemini-3-5-flash']['redirects_to'], 'gemini-3.6-flash')
        self.assertNotIn('google--gemini-3-7-flash', rows['google--gemini-3-6-3-7-3-8-flash-promo']['model_ids'])
        self.assertEqual(len(self.models), 69)
        self.assertEqual(len(self.rates), 63)

    def test_minimax_open_and_rates(self):
        for mid in ('minimax--m2-7', 'minimax--m2-7-highspeed', 'minimax--m3'):
            self.assertEqual(self.models[mid]['openness'], 'Open')
        self.assertEqual(self.models['minimax--m2-7']['total_parameters_b'], 230)
        self.assertEqual(self.models['minimax--m2-7']['active_parameters_b'], 10)
        self.assertEqual(self.models['minimax--m3']['total_parameters_b'], 428)
        self.assertEqual(self.models['minimax--m3']['active_parameters_b'], 23)
        self.assertEqual(self.models['minimax--m2-7-highspeed']['hosted_variant_of'], 'minimax--m2-7')
        rows = {p['id']: p for p in self.rates}
        self.assertEqual(rows['minimax--m3-standard']['input'], 0.30)
        self.assertEqual(rows['minimax--m3-standard']['cached_input'], 0.06)
        self.assertEqual(rows['minimax--m3-priority']['output'], 1.80)
        self.assertEqual(rows['minimax--m3-priority']['context_tiers'][0]['input'], 0.90)
        self.assertEqual(rows['minimax--m2-7-highspeed']['cached_input'], 0.06)
        self.assertEqual(rows['minimax--m2-7-highspeed']['cache_write'], 0.375)
        self.assertEqual(len(self.models), 72)
        self.assertEqual(len(self.rates), 67)
        tab=make_table()
        self.assertIn('| MiniMax | MiniMax M3 | Open |', tab)
        self.assertIn('| MiniMax | MiniMax M3 — Priority | Open |', tab)

    def test_table_row_count(self):
        table=make_table()
        self.assertEqual(len(table.splitlines()),len(self.rates)+2)

if __name__=='__main__':
    unittest.main()
