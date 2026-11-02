# LeetCode 21 — Merge Two Sorted Lists

## Problem
Two singly linked lists are each sorted in increasing order. Combine
them into one sorted list, reusing the existing nodes instead of
building new ones.

## Approach
Use a dummy node in front of the result so the head needs no special
case. Walk both lists with a tail pointer: at each step, attach the
smaller current node and advance that list. When one list is exhausted,
attach the remainder of the other list as-is.

## Complexity
- Time: O(m + n), one pass over both lists.
- Space: O(1) extra space — nodes are reused, not copied.
