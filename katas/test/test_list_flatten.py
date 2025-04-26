import unittest
from katas.list_flatten import flatten_list

class TestListFlatten(unittest.TestCase):
    def test_flatten_list_1(self):
        self.assertEqual(flatten_list([]), [])

    def test_flatten_list_2(self):
        self.assertEqual(flatten_list([1]), [1])

    def test_flatten_list_3(self):
        self.assertEqual(flatten_list([1, 2]), [1, 2])

    def test_flatten_list_4(self):
        self.assertEqual(flatten_list([[1, 2], [3]]), [1, 2, 3])
