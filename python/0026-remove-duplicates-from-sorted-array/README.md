# LeetCode 26: Remove Duplicates from Sorted Array

## Problem (in my own words)

You are given a list of integers sorted in non-decreasing order, so any
repeated values sit next to each other. Remove the duplicates in place:
shift the distinct values to the front of the list, in their original
order, and return how many distinct values there are. The entries after
that count do not matter.

## Approach

Two pointers, one pass:

1. Keep a `write` index pointing at the last unique value kept so far
   (starting at the first element).
2. Scan the rest of the list with a `read` index.
3. Whenever the value at `read` differs from the value at `write`, a new
   unique value has been found: advance `write` by one and copy the new
   value there.
4. Return `write + 1`, the count of unique values now occupying the
   front of the list.

Because the input is sorted, every duplicate of a value appears right
after it, so a single comparison against the last kept value is enough
to spot each new distinct value.

## Complexity

- Time: O(n) — one pass over the array.
- Space: O(1) — only two index variables, modifying the list in place.
