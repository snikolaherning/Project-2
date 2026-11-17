import unittest
from pathlib import Path
from streamlit.testing.v1 import AppTest
class AppTests(unittest.TestCase):
    def test_controls_and_verdicts(self):
        a=AppTest.from_file(str(Path(__file__).resolve().parents[1]/'app.py')).run()
        self.assertFalse(a.exception)
        self.assertEqual(len(a.dataframe),1)
        a.checkbox[0].check().run()
        a.checkbox[1].check().run()
        self.assertFalse(a.exception)
        self.assertIn('4.77%',a.dataframe[0].value['Net estimate'].tolist())
