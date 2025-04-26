import unittest
from katas.reduce_list import reduce_array

class TestReduceList(unittest.TestCase):
    def test_reduce_array_1(self):
        self.assertEqual(reduce_array([]), [])

    def test_reduce_array_2(self):
        self.assertEqual(reduce_array([1, 2, 3]), [1, 1, 1])

    def test_reduce_array_3(self):
        self.assertEqual(reduce_array([1, 10, -2, 17]), [1, 9, -12, 19])