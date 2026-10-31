# LeetCode 20: Valid Parentheses

## Problem (in my own words)

Given a string made up only of the characters `()`, `[]`, and `{}`,
decide whether the brackets are properly balanced: every opening bracket
must be closed by the same kind of bracket, and closers must appear in
the reverse order of their openers (so `([)]` is not valid, but `{[]}`
is).

## Approach

Walk the string once, using a stack. Push each opening bracket onto the
stack. When a closing bracket appears, pop the top of the stack and
check it is the matching opener — if the stack is empty or the types
don't match, the string is invalid. After the whole string, it is valid
only if the stack is empty (no unclosed openers left).

## Complexity

- Time: O(n), a single pass over the string.
- Space: O(n) in the worst case, when the string is all opening brackets.
