import unittest
from katas.requirements_coverage import select_minimal_test_cases

class TestRequirementsCoverage(unittest.TestCase):
    def test_select_minimal_test_cases1(self):
        test_cases = [
            [1, 2, 3],
            [1, 4],
            [2, 3, 4],
            [1, 5],
            [3, 5]
        ]
        self.assertEqual(set(select_minimal_test_cases(test_cases)), {2,3})

    def test_select_minimal_test_cases2(self):
        test_cases = [
            [1, 2, 3, 4]
        ]
        self.assertEqual(set(select_minimal_test_cases(test_cases)), {0})

    def test_select_minimal_test_cases3(self):
        test_cases = [
            [1, 2],
            [2, 3],
            [1, 3]
        ]
        self.assertEqual(set(select_minimal_test_cases(test_cases)) in [{0, 1}, {1, 2}], True)