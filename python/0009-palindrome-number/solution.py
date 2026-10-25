"""LeetCode 9 - Palindrome Number.

Given an integer x, return True if x reads the same forwards and
backwards, and False otherwise.

Approach
--------
Reverse only the second half of the digits and compare it with the
first half. A negative number can never be a palindrome (it starts
with '-'), and any non-zero number ending in 0 can't be one either
(it would have to start with 0).

While the reversed half is smaller than the remaining half, pop the
last digit off x and append it to the reversed half. When the loop
stops, x holds the first half and the reversed half holds the second
half (possibly with one extra middle digit for odd-length numbers,
which we drop with integer division by 10).

Time complexity: O(log10(x)) — one step per digit.
Space complexity: O(1) — only a couple of integer variables.
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negatives and numbers ending in 0 (other than 0 itself)
        # can never read the same backwards.
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10

        # Even length: halves must match. Odd length: drop the middle
        # digit of the reversed half before comparing.
        return x == reversed_half or x == reversed_half // 10


if __name__ == "__main__":
    s = Solution()
    assert s.isPalindrome(121) is True
    assert s.isPalindrome(-121) is False
    assert s.isPalindrome(10) is False
    assert s.isPalindrome(0) is True
    assert s.isPalindrome(1221) is True
    assert s.isPalindrome(12321) is True
    assert s.isPalindrome(123) is False
    assert s.isPalindrome(1000021) is False
    assert s.isPalindrome(1000000001) is True
    assert s.isPalindrome(9) is True
    print("All self-checks passed.")
