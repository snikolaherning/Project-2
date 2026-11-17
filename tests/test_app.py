import unittest
from pathlib import Path
from streamlit.testing.v1 import AppTest
class AppTests(unittest.TestCase):
    def test_controls_and_verdicts(self):
        a=AppTest.from_file(str(Path(__file__).resolve().parents[1]/'app.py'),default_timeout=30).run()
        self.assertFalse(a.exception)
        self.assertEqual(len(a.dataframe),2)
        base=a.dataframe[0].value
        self.assertIn('FAIL',base['Numerical screen'].tolist())
        a.checkbox[0].check().run()
        a.checkbox[1].check().run()
        self.assertFalse(a.exception)
        self.assertIn('4.77%',a.dataframe[0].value['Net estimate'].tolist())
        a.number_input[0].set_value(4.5).run()
        self.assertTrue(any('4.5%' in x.value for x in a.markdown))
        a.slider[0].set_value(100).run()
        self.assertTrue(any('no feasible' in x.value for x in a.error))
        self.assertFalse(a.exception)
