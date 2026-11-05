# LeetCode 35: Search Insert Position

## Problem (in my own words)

You are given a list of distinct numbers that is already sorted from
smallest to largest, plus a target number. Find where the target sits
in the list. If the target is not in the list, say where it would have
to go so the list stays sorted — that is, how many elements are
smaller than it.

## Approach

Use binary search. Keep a window between a low and a high index and
repeatedly look at the middle element:

- If it equals the target, that index is the answer.
- If it is smaller than the target, the answer must be to the right,
  so move the low end past the middle.
- If it is larger, the answer must be to the left, so move the high
  end before the middle.

When the window closes, the low index is exactly the insertion point:
everything before it is smaller than the target, and everything from
it onward is larger.

## Complexity

- Time: O(log n) — the search window halves on every step.
- Space: O(1) — only a few index variables are used.
