import unittest
from katas.max_storage_capacity import max_storage_area

class TestMaxStorageArea(unittest.TestCase):
    def test_max_storage_area1(self):
        self.assertEqual(max_storage_area([2, 1, 5, 6, 2, 3]), 10)

    def test_max_storage_area2(self):
        self.assertEqual(max_storage_area([3, 3, 3, 3]), 12)

    def test_max_storage_area3(self):
        self.assertEqual(max_storage_area([2]), 2)

    def test_max_storage_area4(self):
        self.assertEqual(max_storage_area([6, 2, 5, 4, 5, 1, 6]), 12)