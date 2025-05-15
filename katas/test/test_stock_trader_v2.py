import unittest
from katas.stock_trader_v2 import max_profit

class TestMaxProfit(unittest.TestCase):
    def test_max_profit_1(self):
        self.assertEqual(max_profit([1, 2, 3, 4, 5]), 4)

    def test_max_profit_2(self):
        self.assertEqual(max_profit([7, 6, 4, 3, 1]), 0)

    def test_max_profit_3(self):
        self.assertEqual(max_profit([]), 0)