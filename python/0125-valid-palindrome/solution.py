"""
LeetCode 125 — Valid Palindrome.

Approach: two pointers, one at each end of the string. Move each pointer
inward past any character that is not a letter or digit, then compare the
two characters case-insensitively. If any pair mismatches, the string is
not a palindrome; if the pointers cross, it is.

Time complexity: O(n) — each character is visited at most once.
Space complexity: O(1) — only the two pointers are used.
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True


if __name__ == "__main__":
    sol = Solution()
    assert sol.isPalindrome("A man, a plan, a canal: Panama") is True
    assert sol.isPalindrome("race a car") is False
    assert sol.isPalindrome(" ") is True
    assert sol.isPalindrome("No 'x' in Nixon") is True
    assert sol.isPalindrome("ab") is False
    assert sol.isPalindrome("a") is True
    assert sol.isPalindrome("") is True
    assert sol.isPalindrome("0P") is False
    print("All checks passed.")
