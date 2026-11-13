# LeetCode 53 — Maximum Subarray

## Problem

Given a list of integers (positive and negative), find the contiguous
subarray with the largest sum and return that sum. The subarray must
contain at least one element.

## Approach

Kadane's algorithm: scan the array once while tracking the best subarray
sum that ends at the current position. At each element, either extend the
running subarray with it or start a fresh subarray at it — whichever gives
the larger sum. Keep the best total seen anywhere along the way.

## Complexity

- Time: O(n) — one pass over the array.
- Space: O(1) — only two running variables.
