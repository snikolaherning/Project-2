import unittest
import asof_app as a

class ComparisonTests(unittest.TestCase):
    def test_missing_and_revisions(self):
        h=a.parse_csv('DATE,X\n2020-01-01,1\n2020-02-01,.\n2020-03-01,2\n')
        c=a.parse_csv('DATE,X\n2020-01-01,1.1\n2020-02-01,4\n2020-03-01,2\n2020-04-01,3\n')
        r=a.compare(c,h)
        self.assertEqual(r['Later observations'],1)
        self.assertEqual(r['Revised common dates'],1)
        self.assertEqual(r['Known value'],2)
    def test_duplicate_refused(self):
        with self.assertRaises(ValueError):a.parse_csv('DATE,X\n2020-01-01,1\n2020-01-01,2\n')
    def test_no_known_observations(self):
        c=a.parse_csv('DATE,X\n2020-01-01,1\n')
        r=a.compare(c,c.iloc[:0]);self.assertIsNone(r['Known measured date']);self.assertIsNone(r['Later observations'])

if __name__=='__main__':unittest.main()
