import unittest
from katas.sum_of_digits import sum_of_digits

class TestSumOfDigits(unittest.TestCase):
    def test_sum_of_digits_1(self):
        self.assertEqual(sum_of_digits("1"), 1)

    def test_sum_of_digits_2(self):
        self.assertEqual(sum_of_digits("abc1"), 1)

    def test_sum_of_digits_3(self):
        self.assertEqual(sum_of_digits("abc"), 0)

    def test_sum_of_digits_4(self):
        self.assertEqual(sum_of_digits("a1b2c3"), 6)

    def test_sum_of_digits_5(self):
        self.assertEqual(sum_of_digits(""), 0)