import unittest
from katas.test_case_grouping import group_test_cases

class TestGroupTestCases(unittest.TestCase):
    def test_group_test_cases(self):
        input_sizes = [1, 2, 3, 3, 3, 2]
        result = group_test_cases(input_sizes)
        flattened = [i for group in result for i in group]
        assert sorted(flattened) == list(range(len(input_sizes)))
        for group in result:
            size = input_sizes[group[0]]
            assert len(group) == size
            assert all(input_sizes[i] == size for i in group)
