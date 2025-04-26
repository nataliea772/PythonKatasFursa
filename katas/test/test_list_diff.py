import unittest
from katas.list_diff import find_difference

class TestFindDiff(unittest.TestCase):
    def test_find_difference_1(self):
        self.assertEqual(find_difference([]), 0)

    def test_find_difference_2(self):
        self.assertEqual(find_difference([10]), 0)

    def test_find_difference_3(self):
        self.assertEqual(find_difference([10, 20, -1, 0]), 21)

    def test_find_difference_4(self):
        self.assertEqual(find_difference([9, 5, -1, 0, -4]), 13)
