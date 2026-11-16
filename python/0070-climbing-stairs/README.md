# LeetCode 70 — Climbing Stairs

You are climbing a staircase with `n` steps. Each time you can climb
1 or 2 steps. In how many distinct ways can you climb to the top?

To reach step `n` you must come from step `n-1` (one step) or step
`n-2` (two steps), so the count follows the Fibonacci recurrence:
`ways(n) = ways(n-1) + ways(n-2)`, with `ways(1) = 1` and `ways(2) = 2`.
Iterating with two variables keeps it O(1) space.

- Time: O(n)
- Space: O(1)

Examples: `n = 2` → `2`; `n = 3` → `3`; `n = 5` → `8`.
