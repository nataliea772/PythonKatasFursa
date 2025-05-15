import unittest
from katas.stock_trader import max_profit

class TestStockTrader(unittest.TestCase):
    def test_max_profit_1(self):
        self.assertEqual(max_profit([7, 1, 5, 3, 6, 4]), 5)

    def test_max_profit_2(self):
        self.assertEqual(max_profit([7, 6, 4, 3, 1]), 0)

    def test_max_profit_3(self):
        self.assertEqual(max_profit([5]), 0)