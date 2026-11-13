# LeetCode 58 — Length of Last Word

Given a string of words separated by spaces, return the length of the
last word. Trailing spaces do not count.

Scan from the end: skip any trailing spaces, then count characters
until the next space (or the start of the string).

- Time: O(n)
- Space: O(1) extra

Examples: `"Hello World"` → `5`; `"   fly me   to   the moon  "` → `4` (last word `"moon"`); `"luffy is still joyboy"` → `6`.
