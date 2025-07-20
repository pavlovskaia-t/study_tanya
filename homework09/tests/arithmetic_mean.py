from  homework09.homeworks import asd
import unittest

class MyTest(unittest.TestCase):
    def test_min(self):
        actual_result = asd(-17,-23)
        expected_result = -20
        self.assertEqual(actual_result,expected_result)
    def test_zero(self):
        actual_result = asd(0,0)
        expected_result = 0
        self.assertEqual(actual_result,expected_result)
    def test_float(self):
        actual_result = asd(67.6,26.49)
        expected_result = 47
        self.assertAlmostEqual(actual_result,expected_result,delta=1)
    def test_max(self):
        actual_result = asd(765765886,87654754)
        expected_result = 426710320
        self.assertEqual(actual_result,expected_result)
if __name__ == '__main__':
    unittest.main()