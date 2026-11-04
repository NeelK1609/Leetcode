class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0
        for x in nums:
            if x != val:
                nums[k] = x
                k += 1
        return k


if __name__ == "__main__":
    sol = Solution()
    # LeetCode 27 examples + edge cases; check returned k and first k entries in place.
    nums = [3, 2, 2, 3]
    assert sol.removeElement(nums, 3) == 2 and nums[:2] == [2, 2]
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    assert sol.removeElement(nums, 2) == 5 and nums[:5] == [0, 1, 3, 0, 4]
    nums = [1]
    assert sol.removeElement(nums, 1) == 0
    nums = [1, 2, 3]
    assert sol.removeElement(nums, 4) == 3 and nums[:3] == [1, 2, 3]
    nums = [2, 2, 2]
    assert sol.removeElement(nums, 2) == 0
    nums = []
    assert sol.removeElement(nums, 1) == 0
    print("All 6 checks passed.")
