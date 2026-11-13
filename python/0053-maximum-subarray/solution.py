from typing import List


class Solution:
    """LeetCode 53 — Maximum Subarray.

    Approach: Kadane's algorithm. Walk the array once, keeping the best
    subarray sum ending at the current position. At each step either extend
    the running subarray or start fresh at the current element, whichever
    gives the larger sum; track the best sum seen anywhere.

    Time complexity: O(n) — a single pass over the array.
    Space complexity: O(1) — only two running variables.
    """

    def maxSubArray(self, nums: List[int]) -> int:
        best = current = nums[0]
        for x in nums[1:]:
            current = max(x, current + x)
            best = max(best, current)
        return best


if __name__ == "__main__":
    s = Solution()
    assert s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert s.maxSubArray([1]) == 1
    assert s.maxSubArray([5, 4, -1, 7, 8]) == 23
    assert s.maxSubArray([-1]) == -1
    assert s.maxSubArray([-2, -1]) == -1
    assert s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4, 0]) == 6
    print("All self-checks passed.")
