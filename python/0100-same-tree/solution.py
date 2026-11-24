"""LeetCode 100 — Same Tree.

Approach: recursive structural comparison. Two trees are the same
when both nodes are missing, or both exist with equal values and
their left subtrees match and their right subtrees match. Any
mismatch in value, shape, or a missing node on one side fails fast.

Time: O(n) — each pair of nodes is compared once.
Space: O(h) — recursion depth is the tree height (O(n) worst case
for a skewed tree, O(log n) for a balanced one).
"""


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


def _from_list(values):
    """Build a binary tree from a level-order list (None = missing)."""
    if not values:
        return None
    nodes = [None if v is None else TreeNode(v) for v in values]
    child = 1
    for node in nodes:
        if node is None:
            continue
        if child < len(nodes):
            node.left = nodes[child]
            child += 1
        if child < len(nodes):
            node.right = nodes[child]
            child += 1
    return nodes[0]


if __name__ == "__main__":
    sol = Solution()
    # LeetCode 100 examples + edge cases.
    assert sol.isSameTree(_from_list([1, 2, 3]), _from_list([1, 2, 3])) is True
    assert sol.isSameTree(_from_list([1, 2]), _from_list([1, None, 2])) is False
    assert sol.isSameTree(_from_list([1, 2, 1]), _from_list([1, 1, 2])) is False
    assert sol.isSameTree(None, None) is True
    assert sol.isSameTree(_from_list([1]), None) is False
    assert sol.isSameTree(None, _from_list([1])) is False
    assert sol.isSameTree(_from_list([1]), _from_list([1])) is True
    assert sol.isSameTree(_from_list([1, 2, 3, 4]), _from_list([1, 2, 3, 5])) is False
    print("All 8 checks passed.")
