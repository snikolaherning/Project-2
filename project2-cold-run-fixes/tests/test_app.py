import unittest
from pathlib import Path
from streamlit.testing.v1 import AppTest
class AppTests(unittest.TestCase):
    def test_controls_and_verdicts(self):
        a=AppTest.from_file(str(Path(__file__).resolve().parents[1]/'app.py'),default_timeout=30).run()
        self.assertFalse(a.exception)
        self.assertEqual(len(a.dataframe),2)
        self.assertTrue(any('REJECT 85/15 under these inputs' in x.value for x in a.markdown))
        base=a.dataframe[0].value
        self.assertIn('FAIL',base['Numerical screen'].tolist())
        a.checkbox[0].check().run()
        self.assertTrue(any('PILOT 85/15 in simulation only' in x.value for x in a.markdown))
        a.checkbox[1].check().run()
        self.assertFalse(a.exception)
        self.assertIn('4.77%',a.dataframe[0].value['Net estimate'].tolist())
        a.number_input[0].set_value(4.5).run()
        self.assertTrue(any('4.5%' in x.value for x in a.markdown))
        a.slider[0].set_value(100).run()
        self.assertTrue(any('no feasible' in x.value for x in a.error))
        self.assertFalse(a.exception)

    def test_decision_stops_and_fingerprint(self):
        import committee
        result=committee.run(reserve=1)
        self.assertIn('STOP this scenario',committee.decision_for(result)['action'])
        self.assertEqual(committee.decision_for(result)['live_allocation'],0)
        self.assertEqual(len(result['build_sha256']),64)
