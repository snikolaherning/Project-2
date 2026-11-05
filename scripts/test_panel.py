"""Behavior checks: reference answer, missing inputs, threshold probe, all memos."""
import copy
import json
import unittest
from pathlib import Path
import panel


class PanelTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cost = panel.analyze_panel('COST')
        cls.nvda = panel.analyze_panel('NVDA')

    def test_reference_answer(self):
        self.assertEqual([round(r['current_ratio']['value'], 2) for r in self.cost['rows']], [1.02, 1.07, .97, 1.03, 1.06])
        self.assertEqual([round(r['liabilities_to_equity']['value'], 2) for r in self.cost['rows']], [2.11, 1.75, 1.96, 1.64, 1.49])
        self.assertEqual([list(checks.values()) for checks in self.cost['panel'].values()],
                         [['pass'] * 3, ['fail', 'pass', 'pass'], ['pass'] * 2])

    def test_threshold_boundary_and_gaps(self):
        rows = copy.deepcopy(self.cost['rows'])
        rows[-1]['current_ratio']['value'] = 2.0
        self.assertEqual(next(iter(panel.wood_checks(rows, 2).values())), 'pass')
        rows[-1]['current_ratio']['value'] = None
        rows[0]['net_income']['value'] = None
        self.assertEqual(list(panel.wood_checks(rows, 2).values()), ['not known'] * 3)
        rows[-1]['liabilities']['value'] = None
        self.assertEqual(list(panel.burry_checks(rows).values()), ['not known', 'not known'])

    def test_jpm_gaps_preserved(self):
        result = panel.analyze_panel('JPM')
        self.assertTrue(all(r['capital_spending']['value'] is None for r in result['rows']))
        self.assertEqual(list(result['panel']['Buffett'].values())[1:], ['not known', 'not known'])

    def test_memos_and_independent_number_injection(self):
        for result in [self.cost, self.nvda]:
            for investor in panel.INVESTORS:
                memo = panel.memo_path(result['ticker'], investor).read_text()
                self.assertEqual(panel.unsupported_numbers(memo, result), [], (result['ticker'], investor))
                self.assertIn('40.0%', panel.unsupported_numbers(memo + '\nROE 40.0%', result))
                self.assertIn(panel.verdict(memo), ['own the business', 'watch it', 'pass'])

    def test_nvda_divergence_and_missing_owner_earnings(self):
        self.assertEqual(list(self.nvda['panel']['Cathie Wood'].values()), ['pass'] * 3)
        self.assertEqual(list(self.nvda['panel']['Burry'].values()), ['fail', 'pass'])
        self.assertEqual(list(self.nvda['panel']['Buffett'].values()), ['pass', 'not known', 'not known'])


if __name__ == '__main__':
    unittest.main()
