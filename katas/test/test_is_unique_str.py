import unittest
from katas.is_unique_str import is_unique

class TestIsUniqueStr(unittest.TestCase):
    def test_is_unique(self):
        self.assertEqual(is_unique("Mama"), False)
        self.assertEqual(is_unique("23"), False)
        self.assertEqual(is_unique("world"), True)