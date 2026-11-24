# LeetCode 100 — Same Tree

## Problem

Given the roots of two binary trees `p` and `q`, return `true` if the
two trees are the same — identical in structure and node values — and
`false` otherwise.

## Approach

Recursive structural comparison. Two trees are the same when both
nodes are missing, or both exist with equal values and their left
subtrees match and their right subtrees match. Any mismatch in value,
shape, or a missing node on one side fails fast.

## Complexity

- Time: O(n) — every pair of nodes is compared once.
- Space: O(h) — recursion depth is the tree height (O(log n)
  balanced, O(n) skewed).
