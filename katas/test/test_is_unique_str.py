import unittest
from katas.is_unique_str import is_unique

class TestIsUniqueStr(unittest.TestCase):
    def test_is_unique_1(self):
        self.assertEqual(is_unique("Mama"), False)

    def test_is_unique_2(self):
        self.assertEqual(is_unique("23"), False)

    def test_is_unique_3(self):
        self.assertEqual(is_unique("world"), True)
