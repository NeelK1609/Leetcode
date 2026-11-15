"""LeetCode 66 — Plus One.

Problem (in my own words): a non-negative integer is given as a list of its
decimal digits, most significant digit first, with no leading zeros except
the number zero itself. Add one to the number and return the digits of the
result.

Approach: walk the digits from right to left. If a digit is less than 9,
increment it and we are done — nothing to the left changes. If a digit is
9, it becomes 0 and the carry moves left. If every digit was 9, the result
has one more digit: a leading 1 followed by all zeros.

Time complexity: O(n), one pass from the end in the worst case.
Space complexity: O(1) extra (besides the output list).
"""


class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + [0] * len(digits)


if __name__ == "__main__":
    s = Solution()
    assert s.plusOne([1, 2, 3]) == [1, 2, 4]
    assert s.plusOne([4, 3, 2, 1]) == [4, 3, 2, 2]
    assert s.plusOne([9]) == [1, 0]
    assert s.plusOne([9, 9, 9]) == [1, 0, 0, 0]
    assert s.plusOne([0]) == [1]
    assert s.plusOne([1, 9, 9]) == [2, 0, 0]
    print("All Plus One checks passed.")
