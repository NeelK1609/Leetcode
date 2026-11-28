# LeetCode Practice

Daily coding practice — one LeetCode problem (or a real code change) every day.

## Structure

- `src/` — original Java solutions from 2022 (Eclipse project, kept as-is).
- `python/` — daily Python practice, started October 23, 2026. Each problem lives in its own folder (`NNNN-problem-slug/`) with a `solution.py` and a short `README.md` covering the approach and complexity.

## Progress

| # | Problem | Difficulty | Approach | Solution |
|---|---------|-----------|----------|----------|
| 1 | Two Sum | Easy | Hash map, one pass — O(n) | [python/0001-two-sum](python/0001-two-sum) |
| 9 | Palindrome Number | Easy | Reverse half the digits — O(log x) | [python/0009-palindrome-number](python/0009-palindrome-number) |
| 13 | Roman to Integer | Easy | Subtractive pairs in one pass — O(n) | [python/0013-roman-to-integer](python/0013-roman-to-integer) |
| 14 | Longest Common Prefix | Easy | Shrink first string until all share it — O(S) | [python/0014-longest-common-prefix](python/0014-longest-common-prefix) |
| 20 | Valid Parentheses | Easy | Stack matching — O(n) | [python/0020-valid-parentheses](python/0020-valid-parentheses) |
| 21 | Merge Two Sorted Lists | Easy | Dummy node, merge in one pass — O(m + n) | [python/0021-merge-two-sorted-lists](python/0021-merge-two-sorted-lists) |
| 26 | Remove Duplicates from Sorted Array | Easy | Two pointers, in-place — O(n) | [python/0026-remove-duplicates-from-sorted-array](python/0026-remove-duplicates-from-sorted-array) |
| 27 | Remove Element | Easy | Two-pointer in-place overwrite — O(n) | [python/0027-remove-element](python/0027-remove-element) |
| 35 | Search Insert Position | Easy | Binary search, return lo as insertion point — O(log n) | [python/0035-search-insert-position](python/0035-search-insert-position) |
| 53 | Maximum Subarray | Medium | Kadane's algorithm, one pass — O(n) | [python/0053-maximum-subarray](python/0053-maximum-subarray) |
| 58 | Length of Last Word | Easy | Scan from the end, skip trailing spaces — O(n) | [python/0058-length-of-last-word](python/0058-length-of-last-word) |
| 66 | Plus One | Easy | Add one from the right, carry 9s — O(n) | [python/0066-plus-one](python/0066-plus-one) |
| 70 | Climbing Stairs | Easy | Fibonacci recurrence, two variables — O(n) | [python/0070-climbing-stairs](python/0070-climbing-stairs) |
| 83 | Remove Duplicates from Sorted List | Easy | Skip duplicate neighbours in one pass — O(n) | [python/0083-remove-duplicates-from-sorted-list](python/0083-remove-duplicates-from-sorted-list) |
| 88 | Merge Sorted Array | Easy | Merge from the back, in place — O(m + n) | [python/0088-merge-sorted-array](python/0088-merge-sorted-array) |
| 94 | Binary Tree Inorder Traversal | Easy | Iterative stack, left-root-right — O(n) | [python/0094-binary-tree-inorder-traversal](python/0094-binary-tree-inorder-traversal) |
| 100 | Same Tree | Easy | Recursive structural comparison — O(n) | [python/0100-same-tree](python/0100-same-tree) |
| 104 | Maximum Depth of Binary Tree | Easy | Recursive DFS, 1 + max(left, right) — O(n) | [python/0104-maximum-depth-of-binary-tree](python/0104-maximum-depth-of-binary-tree) |
| 121 | Best Time to Buy and Sell Stock | Easy | Track lowest price, best profit in one pass — O(n) | [python/0121-best-time-to-buy-and-sell-stock](python/0121-best-time-to-buy-and-sell-stock) |
| 125 | Valid Palindrome | Easy | Two pointers, skip non-alphanumerics — O(n) | [python/0125-valid-palindrome](python/0125-valid-palindrome) |
