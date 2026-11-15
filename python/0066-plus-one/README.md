# LeetCode 66 — Plus One

## Problem
A non-negative integer is given as a list of its decimal digits, most
significant digit first. Add one to the number and return the digits of
the result.

## Approach
Walk the digits from right to left. If a digit is less than 9, increment
it and stop — nothing to the left changes. If a digit is 9, it becomes 0
and the carry moves one place left. If every digit was 9, the result gains
a leading 1 followed by all zeros.

## Complexity
- Time: O(n) — a single pass from the end in the worst case.
- Space: O(1) extra, besides the output list.
