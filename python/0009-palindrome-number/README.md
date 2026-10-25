# LeetCode 9 — Palindrome Number

## Problem

Given an integer, decide whether it reads the same forwards and
backwards. For example, 121 reads the same either way, while −121
does not (the minus sign breaks the mirror) and 10 does not (it
would have to start with 0 to end with 0).

## Approach

Instead of converting the number to a string, work with the digits
directly: peel digits off the end of the number and build up a
reversed copy of the second half. Stop once the reversed half is at
least as big as what remains — at that point the remaining part is
the first half. The number is a palindrome when the two halves
match; for odd-length numbers, drop the middle digit of the reversed
half before comparing.

Two quick rejections up front: any negative number, and any non-zero
number ending in 0.

## Complexity

- Time: O(log₁₀ x) — one step per digit.
- Space: O(1) — only a few integer variables.
