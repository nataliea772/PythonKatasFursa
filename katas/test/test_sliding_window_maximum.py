import unittest
from katas.sliding_window_maximum import max_sliding_window

class TestMaxSlidingWindow(unittest.TestCase):
    def test_max_sliding_window1(self):
        nums = [1, 3, -1, -3, 5, 3, 6, 7]
        k = 3
        expected = [3, 3, 5, 5, 6, 7]
        self.assertEqual(max_sliding_window(nums, k), expected)

    def test_max_sliding_window2(self):
        nums = [1, -1]
        k = 1
        expected = [1, -1]
        self.assertEqual(max_sliding_window(nums, k), expected)

    def test_max_sliding_window3(self):
        nums = [4, 2, 12, 11]
        k = 4
        expected = [12]
        self.assertEqual(max_sliding_window(nums, k), expected)
