# LeetCode 83 — Remove Duplicates from Sorted List

Given the head of a sorted linked list, delete all duplicates so each
value appears only once, and return the list still sorted.

Because the list is sorted, duplicates are always neighbours. Walk the
list once with a single pointer: if the current node and the next node
hold the same value, skip the next node by pointing past it; otherwise
move on. The list is edited in place, with no extra storage.

- Time: O(n)
- Space: O(1)

Examples: `[1, 1, 2]` → `[1, 2]`; `[1, 1, 2, 3, 3]` → `[1, 2, 3]`.
