"""LeetCode 26: Remove Duplicates from Sorted Array.

Approach: two pointers. Keep a write index at the position of the last
unique value seen. Scan the array with a read index; whenever the current
value differs from the value at the write index, advance the write index
and copy the new unique value there. The first ``k`` entries then hold
the unique values in order, and ``k`` is the answer.

Time complexity: O(n) — a single pass over the array.
Space complexity: O(1) — only two index variables are used.
"""


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0
        write = 0
        for read in range(1, len(nums)):
            if nums[read] != nums[write]:
                write += 1
                nums[write] = nums[read]
        return write + 1


if __name__ == "__main__":
    sol = Solution()

    nums = [1, 1, 2]
    k = sol.removeDuplicates(nums)
    assert k == 2 and nums[:k] == [1, 2], (k, nums[:k])

    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k = sol.removeDuplicates(nums)
    assert k == 5 and nums[:k] == [0, 1, 2, 3, 4], (k, nums[:k])

    nums = []
    assert sol.removeDuplicates(nums) == 0

    nums = [7]
    k = sol.removeDuplicates(nums)
    assert k == 1 and nums[:k] == [7]

    nums = [1, 1, 1, 1]
    k = sol.removeDuplicates(nums)
    assert k == 1 and nums[:k] == [1]

    nums = [-1, 0, 0, 1, 2, 2]
    k = sol.removeDuplicates(nums)
    assert k == 4 and nums[:k] == [-1, 0, 1, 2]

    print("All self-checks passed.")
