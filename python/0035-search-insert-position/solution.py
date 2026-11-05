"""LeetCode 35: Search Insert Position.

Given a sorted list of distinct integers and a target, return the index
of the target if it is present, or the index where it would be inserted
to keep the list sorted.

Approach: classic binary search. Keep a window [lo, hi] and repeatedly
check the middle element. If it equals the target, return its index.
If it is smaller, the answer must lie to the right; otherwise to the
left. When the window closes, lo is exactly the insertion point: every
element before lo is smaller than the target, and every element from
lo on is larger.

Time complexity: O(log n) — the window halves each step.
Space complexity: O(1) — only a few index variables are used.
"""

from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return lo


if __name__ == "__main__":
    s = Solution()
    assert s.searchInsert([1, 3, 5, 6], 5) == 2
    assert s.searchInsert([1, 3, 5, 6], 2) == 1
    assert s.searchInsert([1, 3, 5, 6], 7) == 4
    assert s.searchInsert([1, 3, 5, 6], 0) == 0
    assert s.searchInsert([1], 1) == 0
    assert s.searchInsert([1], 0) == 0
    assert s.searchInsert([1], 2) == 1
    assert s.searchInsert([], 5) == 0
    assert s.searchInsert([1, 3, 5, 6, 8, 10], 9) == 5
    print("All self-checks passed.")
