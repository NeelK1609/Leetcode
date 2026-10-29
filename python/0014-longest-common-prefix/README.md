# LeetCode 14 — Longest Common Prefix

Start with the first string as the candidate prefix, then shrink it
from the end until every other string starts with it. An empty
candidate means there is no common prefix.

- Time: O(S), where S is the total number of characters across all strings
- Space: O(1) extra — the prefix is a slice of an input string

Examples: `["flower", "flow", "flight"]` → `"fl"`, `["dog", "racecar", "car"]` → `""`.
