# LeetCode 13 — Roman to Integer

## Problem

Given a string made of Roman numeral symbols (`I`, `V`, `X`, `L`, `C`, `D`, `M`),
work out the integer it represents. Symbols are normally added together
(`III` = 3), but when a smaller symbol appears just before a larger one,
its value is subtracted instead (`IV` = 4, `IX` = 9, `XL` = 40, `CM` = 900).

## Approach

Walk the string once from left to right with a lookup table of symbol values.
For each symbol, compare it with the one after it: if the next symbol is
larger, subtract the current value; otherwise add it. This handles every
subtractive pair in a single pass without special cases.

## Complexity

- Time: O(n), one pass over the string.
- Space: O(1), the value table has a fixed size of seven symbols.
