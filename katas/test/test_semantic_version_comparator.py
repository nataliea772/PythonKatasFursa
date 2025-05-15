import unittest
from katas.semantic_version_comparator import compare_versions

class TestSemanticVersionComparator(unittest.TestCase):
    def test_compare_versions1(self):
        self.assertEqual(compare_versions('1.0.0', '1.0.0'), 0)
        self.assertEqual(compare_versions('1.1.0', '1.0.0'), 1)
        self.assertEqual(compare_versions('1.0.0', '1.0.1'), -1)

