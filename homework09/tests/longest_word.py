from homework09.homeworks import find_longest_word
import unittest
class MyTest(unittest.TestCase):
    def test_ok(self):
        words = ['Tanya','Robert','Math','Elizabeth','Python']
        actual_result = find_longest_word(words)
        expected_result = 'Elizabeth'
        self.assertEqual(actual_result,expected_result)
    def test_abc(self):
        words = ['abcdef','abc','a']
        actual_result = find_longest_word(words)
        expected_result = 'abcdef'
        self.assertEqual(actual_result,expected_result)
    def test_empty(self):
        words = ['','','','']
        actual_result = find_longest_word(words)
        expected_result = ''
        self.assertEqual(actual_result,expected_result)
    def test_empty2(self):
        words = []
        actual_result = find_longest_word(words)
        expected_result = ''
        self.assertEqual(actual_result,expected_result)
if __name__ == '__main__':
    unittest.main()