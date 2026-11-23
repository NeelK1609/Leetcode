# LeetCode 94 — Binary Tree Inorder Traversal

## Problem

Given the root of a binary tree, return the inorder traversal of its
nodes' values: visit the left subtree, then the node itself, then the
right subtree.

## Approach

Iterative inorder traversal with an explicit stack, instead of
recursion. Walk down the left edge, pushing each node; when there is no
left child left, pop a node, record its value, then move to its right
subtree. Each node is pushed and popped exactly once, so the values
come out in left → root → right order.

## Complexity

- Time: O(n) — every node is visited once.
- Space: O(h) — the stack holds at most the tree height (O(log n)
  balanced, O(n) skewed).
