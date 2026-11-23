"""LeetCode 94 — Binary Tree Inorder Traversal.

Approach: iterative inorder traversal with an explicit stack. Walk
down the left edge, pushing each node; when there is no left child
left, pop a node, record its value, then move to its right subtree.
This visits nodes in left → root → right order, exactly the inorder
sequence, without recursion.

Time: O(n) — each node is pushed and popped once.
Space: O(h) — the stack holds at most the tree height (O(n) worst case
for a skewed tree, O(log n) for a balanced one).
"""


from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []
        current = root
        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            result.append(current.val)
            current = current.right
        return result


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
    # LeetCode 94 examples + edge cases.
    assert sol.inorderTraversal(_from_list([1, None, 2, 3])) == [1, 3, 2]
    assert sol.inorderTraversal(_from_list([])) == []
    assert sol.inorderTraversal(_from_list([1])) == [1]
    assert sol.inorderTraversal(_from_list([1, 2, 3, 4, 5, None, 8])) == [4, 2, 5, 1, 3, 8]
    assert sol.inorderTraversal(_from_list([3, 1, None, None, 2])) == [1, 2, 3]
    assert sol.inorderTraversal(_from_list([1, 2, None, 3])) == [3, 2, 1]
    assert sol.inorderTraversal(_from_list([1, None, 2, None, 3])) == [1, 2, 3]
    assert sol.inorderTraversal(None) == []
    print("All 8 checks passed.")
