# 1. Two Sum (Easy)

**Problem (summary):** Given an array of integers `nums` and an integer `target`, return the indices of the two numbers that add up to `target`. Exactly one solution exists; the same element cannot be used twice.

**Examples:**
- `nums = [2, 7, 11, 15], target = 9` -> `[0, 1]`
- `nums = [3, 2, 4], target = 6` -> `[1, 2]`

**Approach:** One-pass hash map. As we scan, we remember each value and its index. For the current value we look up `target - value` in the map; a hit gives us both indices immediately.

**Complexity:** Time O(n), Space O(n).

**Solution:** [solution.py](solution.py)
