"""LeetCode 1. Two Sum

Given a list of integers `nums` and an integer `target`, return the indices
of the two numbers that add up to `target`. Exactly one solution exists, and
the same element cannot be used twice.

Approach: one-pass hash map. While scanning, store each value's index. For
the current value, check whether `target - value` was already seen; if so,
those two indices are the answer.

Time:  O(n) - single pass, O(1) average lookup.
Space: O(n) - the map holds at most n entries.
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # value -> index
        for i, value in enumerate(nums):
            complement = target - value
            if complement in seen:
                return [seen[complement], i]
            seen[value] = i
        return []  # unreachable under the problem's guarantee


if __name__ == "__main__":
    s = Solution()
    assert s.twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert s.twoSum([3, 2, 4], 6) == [1, 2]
    assert s.twoSum([3, 3], 6) == [0, 1]
    print("All checks passed.")
