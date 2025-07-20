from homework09.homeworks import has_more_than_10_unique_chars
import unittest
class MyTest(unittest.TestCase):
    def test_true(self):
        actual_result = has_more_than_10_unique_chars('qwertyuiokjhgfdszzxcvbnm')
        expected_result = True
        self.assertEqual(actual_result,expected_result)
    def test_false(self):
        actual_result = has_more_than_10_unique_chars('rtgfrtgft')
        expected_result = False
        self.assertEqual(actual_result, expected_result)
    def test_true2(self):
        actual_result = has_more_than_10_unique_chars('@#@#yyn !dyynnyynyyen  ,, ene9983838yyryy')
        expected_result = True
        self.assertEqual(actual_result, expected_result)
    def test_false2(self):
        actual_result = has_more_than_10_unique_chars('')
        expected_result = False
        self.assertEqual(actual_result, expected_result)

if __name__ == '__main__':
    unittest.main()