# LeetCode 125 — Valid Palindrome

## Problem (in my own words)

Given a string, decide whether it reads the same forwards and backwards
once you ignore case and drop every character that isn't a letter or a
digit. Punctuation and spaces don't count, and "A" matches "a".

## Approach

Two pointers, one at each end. Each pointer skips over non-alphanumeric
characters, then the two characters are compared case-insensitively. A
mismatch means "not a palindrome"; if the pointers meet, it is one.

## Complexity

- Time: O(n) — each character is visited at most once.
- Space: O(1) — only the two pointers are used.
