from collections import defaultdict
from reprlib import recursive_repr

from uaclient.util import retry


def is_valid_git_tree(tree_map):
    """
    Determines if a given tree structure represents a valid Git tree.

    A valid Git tree should:
    1. Have exactly one root (no parent).
    2. Contain no cycles.

    Args:
        tree_map: a dictionary representing the Git tree (commit ID to list of child commit IDs)

    Returns:
        True if the tree is a valid Git tree, False otherwise
    """
    # build parent map to find root
    all_nodes = set(tree_map.keys())
    child_nodes = {child for children in tree_map.values() for child in children}
    root_candidates = all_nodes - child_nodes

    # 1 root
    if len(root_candidates) != 1:
        return False

    root = next(iter(root_candidates))

    # DFS - check for cycles
    visited = set()
    recursion_stack = set()

    def dfs(node):
        if node in recursion_stack:
            return False
        elif node in visited:
            return True

        visited.add(node)
        recursion_stack.add(node)
        for child in tree_map.get(node, []):
            if not dfs(child):
                return False
        recursion_stack.remove(node)
        return True

    if not dfs(root):
        return False

    # all nodes are reachable
    if visited != all_nodes:
        return False

    return True


if __name__ == '__main__':
    valid_tree = {
        "A": ["B", "C"],
        "B": ["D"],
        "C": [],
        "D": []
    }

    invalid_tree = {
        "A": ["B"],
        "B": ["C"],
        "C": ["A"]  # cycle
    }

    print(f"Is valid tree: {is_valid_git_tree(valid_tree)}")  # Should be True
    print(f"Is valid tree: {is_valid_git_tree(invalid_tree)}")  # Should be False