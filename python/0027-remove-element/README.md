# LeetCode 27 — Remove Element

Walk the list once, copying every element that is not `val` forward
into the front of the same list. The write index `k` ends up as the
count of kept elements, and the first `k` entries are the result.

- Time: O(n)
- Space: O(1) extra — in-place

Examples: `[3, 2, 2, 3], val = 3` → `k = 2`, first entries `[2, 2]`; `[0, 1, 2, 2, 3, 0, 4, 2], val = 2` → `k = 5`.
