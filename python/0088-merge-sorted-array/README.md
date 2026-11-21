# LeetCode 88 — Merge Sorted Array

## Problem

Two lists are given in non-decreasing order: `nums1` holds its first `m`
values followed by `n` empty slots (zeroes), and `nums2` holds `n` values.
Merge `nums2` into `nums1` so that `nums1` ends up holding all `m + n`
values in non-decreasing order, using only the space already in `nums1`.

## Approach

Merge from the back instead of the front. Keep three pointers: `i` at the
last real value of `nums1`, `j` at the last value of `nums2`, and `k` at
the last slot of `nums1`. At each step, copy the larger of `nums1[i]` and
`nums2[j]` into `nums1[k]` and move the pointers back. Working backwards
means we never overwrite a value of `nums1` that we still need. Once
`nums2` is exhausted we are done — any remaining values of `nums1` are
already in their final positions.

## Complexity

- Time: O(m + n) — every element is moved once.
- Space: O(1) — the merge happens in place.
