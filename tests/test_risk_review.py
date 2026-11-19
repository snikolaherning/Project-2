import unittest
import math
import csv
import json
import calendar
from datetime import datetime,timezone
from pathlib import Path
import committee as c
import risk_review as rr

class DecisionRiskTests(unittest.TestCase):
    def test_bil_exposure_dominates_fixed_return_sensitivity(self):
        self.assertEqual(rr.format_percent(rr.expected_net(.03,.065)),'3.28%')
        base=rr.expected_net(.03,.065)
        self.assertAlmostEqual(rr.expected_net(.04,.065)-base,.0085)
        self.assertAlmostEqual(rr.expected_net(.03,.075)-base,.0015)
    def test_break_even_bridges_back_to_target(self):
        for target in [.045,.05]:
            bil=rr.bil_break_even(target,.065,25)
            self.assertAlmostEqual(rr.expected_net(bil,.065,25),target)
            self.assertLess(rr.expected_net(bil-.0001,.065,25),target)
    def test_crash_probe_refutes_hard_10_percent_guarantee(self):
        x=rr.shock_result([.85,0,0,.15],[0,0,0,-1])
        self.assertAlmostEqual(x['drawdown'],.15)
        self.assertFalse(x['drawdown_screen'])
    def test_spending_is_cash_flow_and_obligation_does_not_shrink(self):
        x=rr.shock_result([.85,0,0,.15],[0,0,0,-.5])
        self.assertAlmostEqual(x['assets_after_market_per_100'],92.5)
        self.assertAlmostEqual(x['assets_after_withdrawal'],87.5)
        self.assertAlmostEqual(x['drawdown'],.075)
        self.assertEqual(x['fixed_spending_obligation'],5)
        self.assertEqual(x['protected_dollars_implemented'],0)
    def test_bil_override_changes_return_not_covariance_or_old_weights(self):
        base=c.run();stress=c.run(bil_return=.02)
        before=base['portfolios']['Student pilot 85/15'];after=stress['portfolios']['Student pilot 85/15']
        change=.85*(.02-base['estimates']['returns'][0])
        self.assertAlmostEqual(after['net_return']-before['net_return'],change)
        self.assertEqual(before['weights'],after['weights'])
        self.assertEqual(before['volatility'],after['volatility'])
    def test_nonfinite_estimate_stops_run(self):
        for value in [float('nan'),float('inf')]:
            with self.assertRaises(ValueError): c.run(bil_return=value)
    def test_actual_vintage_excludes_unavailable_september(self):
        v=rr.signal_snapshot()
        self.assertFalse(v['2026-09-30']['september_observation_present'])
        self.assertEqual(v['2026-09-30']['latest_measured_month'],'2026-08-01')
        self.assertAlmostEqual(v['2026-09-30']['value_percent_per_annum'],3.72)
        self.assertTrue(v['2026-10-29']['september_observation_present'])
        self.assertAlmostEqual(v['2026-10-29']['value_percent_per_annum'],3.94)
    def test_csv_reconstructs_from_raw_adjclose_without_silent_filling(self):
        root=c.ROOT/'Lab15 2'
        with (root/'prices.csv').open() as handle: rows=list(csv.DictReader(handle))
        for ticker in ['BIL','IEF','LQD','VT']:
            raw=json.loads((root/'source-evidence'/f'{ticker}.json').read_text())['chart']['result'][0]
            adj=raw['indicators']['adjclose'][0]['adjclose']
            self.assertEqual(len(rows),len(adj))
            for row,timestamp,value in zip(rows,raw['timestamp'],adj):
                day=datetime.fromtimestamp(timestamp,timezone.utc)
                end=f'{day.year}-{day.month:02d}-{calendar.monthrange(day.year,day.month)[1]}'
                self.assertEqual(row['Date'],end)
                self.assertIsNotNone(value)
                self.assertEqual(float(row[ticker]),value)

    def test_retrospective_split_uses_training_only_for_selection(self):
        import tempfile
        original=rr.temporal_review()
        with c.PRICES.open() as handle:rows=list(csv.reader(handle))
        # Perturb only future prices: selection and training estimates must not change.
        for row in rows[38:]:
            row[4]=str(float(row[4])*.5)
        with tempfile.TemporaryDirectory() as folder:
            path=Path(folder)/'changed.csv'
            with path.open('w') as handle:csv.writer(handle).writerows(rows)
            changed=rr.temporal_review(path)
        self.assertEqual(original['training_estimates'],changed['training_estimates'])
        self.assertEqual(original['training_feasible'],changed['training_feasible'])
        for name,x in original['results'].items():
            self.assertEqual(x['weights'],changed['results'][name]['weights'])
        self.assertEqual(original['training_return_months'],36)
        self.assertEqual(original['test_return_months'],24)
