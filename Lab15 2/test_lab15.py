import copy
import io
import math
import statistics
import unittest
import portfolio as p

class EngineTests(unittest.TestCase):
    def solve(self, returns=None, corr=None, objective=.065):
        return p.search(returns or p.EXPECTED_RETURNS,p.VOLATILITIES,corr or p.CORRELATIONS,objective,.03,[0,1])
    def test_training(self):
        base=self.solve();stress=self.solve(p.EXPECTED_RETURNS[:3]+[.07])
        self.assertEqual(base['weights'],[0,.2,.25,.55])
        self.assertAlmostEqual(base['volatility']*100,9.44,delta=.005)
        self.assertEqual(stress['weights'],[0,.1,.1,.8])
        self.assertAlmostEqual(stress['volatility']*100,12.94,delta=.005)
        self.assertAlmostEqual(p.largest_weight_change(base,stress),25)
    def test_engine_edit(self):
        c=copy.deepcopy(p.CORRELATIONS);c[2][3]=c[3][2]=.5
        result=self.solve(corr=c)
        self.assertEqual(result['weights'],[0,.4,0,.6])
        self.assertAlmostEqual(result['volatility']*100,9.73,delta=.005)
    def test_infeasible(self):
        self.assertIsNone(self.solve(objective=.20))
        self.assertIsNone(p.search(p.EXPECTED_RETURNS,p.VOLATILITIES,p.CORRELATIONS,.065,.03,[]))
    def test_grid_complete(self):
        weights=list(p.grid_weights(4))
        self.assertEqual(len(weights),math.comb(23,3))
        self.assertEqual(len(set(weights)),len(weights))
        for row in weights:self.assertAlmostEqual(sum(row),1)
    def fixture(self):
        rows=['Date,A,B,C'];prices=[100,100,100];actual=[]
        for month in range(61):
            if month:
                rates=[.003+.002*math.sin(month),.004+.003*math.cos(month),.006+.004*math.sin(month*.7)]
                actual.append(rates);prices=[x*(1+r) for x,r in zip(prices,rates)]
            rows.append(f'{2020+month//12}-{month%12+1:02d}-01,'+','.join(map(str,prices)))
        return '\n'.join(rows),actual
    def test_csv_estimates(self):
        raw,actual=self.fixture()
        for recent,count in [(False,60),(True,36)]:
            e=p.estimate_from_csv(io.StringIO(raw),recent)
            self.assertEqual(e['return_months'],count)
            for i in range(3):
                series=[row[i] for row in actual[-count:]]
                self.assertAlmostEqual(e['returns'][i],statistics.mean(series)*12)
                self.assertAlmostEqual(e['volatilities'][i],statistics.stdev(series)*math.sqrt(12))
    def test_bad_csv(self):
        raw,_=self.fixture()
        for bad in [raw.replace('2020-02-01','2020-01-01'),raw.replace('100,100,100','0,100,100'),raw.replace('Date,A,B,C','Date,A,A,C')]:
            with self.assertRaises(ValueError):p.estimate_from_csv(io.StringIO(bad))

if __name__=='__main__':unittest.main()
