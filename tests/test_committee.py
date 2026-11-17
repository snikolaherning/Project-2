import unittest
import committee as c
import portfolio as p
class CommitteeTests(unittest.TestCase):
    def test_known_covariance(self):
        self.assertAlmostEqual(p.portfolio_volatility([.5,.5],[[.04,0],[0,.09]]),(.0325)**.5)
    def test_cost_bridge(self):
        e=dict(returns=[.04,.08],volatilities=[.01,.1],correlations=[[1,0],[0,1]])
        x=c.evaluate([.5,.5],e,25)
        self.assertAlmostEqual(x['net_return'],.0575)
    def test_rules_and_infeasibility(self):
        r=c.run(reserve=1,vt_return=.07)
        self.assertFalse(r['feasible'])
        self.assertFalse(r['portfolios']['60/40 benchmark']['rules']['BIL reserve floor'])
    def test_grid_constraints(self):
        for recent in [False,True]:
            r=c.run(recent)
            x=r['portfolios'].get('Constrained portfolio')
            if x:
                self.assertEqual(x['verdict'],'PASS')
                self.assertAlmostEqual(sum(x['weights']),1)
if __name__=='__main__': unittest.main()

class DrawdownAndSpendingTests(unittest.TestCase):
    def test_peak_to_trough_includes_start(self):
        self.assertAlmostEqual(c.drawdown_path([-.1]),.1)
        self.assertAlmostEqual(c.drawdown_path([.2,-.1,-.1]),.19)
    def test_cash_flow_is_not_return(self):
        # A withdrawal is excluded from unitized returns; a flat investment has no drawdown.
        self.assertEqual(c.drawdown_path([0,0]),0)
    def test_protected_budget_dollars(self):
        self.assertTrue(c.spending_coverage(5,5))
        self.assertFalse(c.spending_coverage(4.99,5))
    def test_drawdown_blocks_benchmark(self):
        x=c.run()['portfolios']['60/40 benchmark']
        self.assertGreater(x['historical_max_drawdown'],.10)
        self.assertFalse(x['rules']['Historical monthly drawdown <= 10%'])
