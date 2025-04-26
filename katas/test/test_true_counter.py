import unittest
from katas.true_counter import count_true_values

class TestTrueCounter(unittest.TestCase):
    def test_true_counter_1(self):
        self.assertEqual(count_true_values([True, False, True, True, False]), 3)

    def test_true_counter_2(self):
        self.assertEqual(count_true_values([False, False, True, False]), 1)

    def test_true_counter_3(self):
        self.assertEqual(count_true_values([True]), 1)
        self.assertEqual(count_true_values([False]), 0)

    def test_true_counter_4(self):
        self.assertEqual(count_true_values([False, False, False]), 0)

    def test_true_counter_5(self):
        self.assertEqual(count_true_values([]), 0)