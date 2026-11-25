# LeetCode 104 — Maximum Depth of Binary Tree

## Problem

Given the root of a binary tree, return its maximum depth — the
number of nodes on the longest path from the root down to the
farthest leaf. An empty tree has depth 0.

## Approach

Recursive depth-first search. An empty tree has depth 0; otherwise
the depth is 1 plus the larger of the depths of the left and right
subtrees, so the recursion follows the longest root-to-leaf path.

## Complexity

- Time: O(n) — every node is visited once.
- Space: O(h) — recursion depth is the tree height (O(log n)
  balanced, O(n) skewed).
