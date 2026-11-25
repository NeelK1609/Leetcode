"""LeetCode 104 — Maximum Depth of Binary Tree.

Approach: recursive depth-first search. An empty tree has depth 0;
otherwise the depth is 1 plus the larger of the depths of the left
and right subtrees. Each node is visited once, and the recursion
follows the longest root-to-leaf path.

Time: O(n) — each node is visited once.
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
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


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
    # LeetCode 104 examples + edge cases.
    assert sol.maxDepth(_from_list([3, 9, 20, None, None, 15, 7])) == 3
    assert sol.maxDepth(_from_list([1, None, 2])) == 2
    assert sol.maxDepth(None) == 0
    assert sol.maxDepth(_from_list([1])) == 1
    assert sol.maxDepth(_from_list([1, 2, 3, 4, 5, 6, 7])) == 3
    assert sol.maxDepth(_from_list([1, 2, 3, 4, 5])) == 3
    assert sol.maxDepth(_from_list([1, None, 2, None, 3, None, 4])) == 4
    assert sol.maxDepth(_from_list([1, 2, None, 3])) == 3
    print("All 8 checks passed.")
