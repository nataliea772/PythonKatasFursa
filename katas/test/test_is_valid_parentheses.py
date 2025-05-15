import unittest
from katas.is_valid_parentheses import is_valid_parentheses

class TestIsValidParentheses(unittest.TestCase):
    def test_is_valid_parentheses1(self):
        self.assertEqual(is_valid_parentheses("[]"), True)

    def test_is_valid_parentheses2(self):
        self.assertEqual(is_valid_parentheses("[({(})]"), False)

    def test_is_valid_parentheses3(self):
        self.assertEqual(is_valid_parentheses("{{()}]"), False)

    def test_is_valid_parentheses4(self):
        self.assertEqual(is_valid_parentheses(""), True)