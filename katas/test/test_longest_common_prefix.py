import unittest
from katas.longest_common_prefix import longest_common_prefix

class TestLongestCommonPrefix(unittest.TestCase):
    def test_longest_common_prefix_empty(self):
        self.assertEqual(longest_common_prefix([]), "")

    def test_longest_common_prefix_1(self):
        self.assertEqual(longest_common_prefix(["", "a", "a", "a"]), "")

    def test_longest_common_prefix_2(self):
        self.assertEqual(longest_common_prefix(["fursa", "Fursa", "Fursa"]), "fursa")

    def test_longest_common_prefix_3(self):
        self.assertEqual(longest_common_prefix(["Natalie", "Nat", "nata"]), "nat")