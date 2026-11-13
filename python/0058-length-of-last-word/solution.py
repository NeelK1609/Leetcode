class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Scan from the end: skip trailing spaces, then count the last word.
        i = len(s) - 1
        while i >= 0 and s[i] == " ":
            i -= 1
        length = 0
        while i >= 0 and s[i] != " ":
            length += 1
            i -= 1
        return length


if __name__ == "__main__":
    sol = Solution()
    # LeetCode 58 examples + edge cases.
    assert sol.lengthOfLastWord("Hello World") == 5
    assert sol.lengthOfLastWord("   fly me   to   the moon  ") == 4
    assert sol.lengthOfLastWord("luffy is still joyboy") == 6
    assert sol.lengthOfLastWord("a") == 1
    assert sol.lengthOfLastWord("a ") == 1
    assert sol.lengthOfLastWord("   a   b   ") == 1
    assert sol.lengthOfLastWord("Hello") == 5
    print("All 7 checks passed.")
