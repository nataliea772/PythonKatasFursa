import unittest
from katas.is_valid_git_tree import is_valid_git_tree

class TestIsValidGitTree(unittest.TestCase):
    def test_is_valid_git_tree1(self):
        tree = {
            "A": ["B", "C"],
            "B": ["D"],
            "C": [],
            "D": []
        }
        self.assertEqual(is_valid_git_tree(tree), True)

    def test_is_valid_git_tree2(self):
        tree = {
            "A": ["B"],
            "B": ["C"],
            "C": ["A"]
        }
        self.assertEqual(is_valid_git_tree(tree), False)

    def test_is_valid_git_tree3(self):
        tree = {
            "A": ["B"],
            "C": ["D"],
            "B": [],
            "D": []
        }
        self.assertEqual(is_valid_git_tree(tree), False)

    def test_is_valid_git_tree4(self):
        tree = {
            "A": ["B"],
            "B": [],
            "C": []
        }
        self.assertEqual(is_valid_git_tree(tree), False)