"""
LeetCode 13 — Roman to Integer.

Convert a Roman numeral string to its integer value.

Approach: scan the string left to right, keeping a lookup of each
symbol's value. A symbol smaller than the one after it is subtracted
(e.g. IV = 4, IX = 9); otherwise it is added. One pass is enough
because each symbol is examined once.

Time complexity: O(n), where n is the length of the string.
Space complexity: O(1) — the value table has a fixed size.
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        values = {"I": 1, "V": 5, "X": 10, "L": 50,
                  "C": 100, "D": 500, "M": 1000}
        total = 0
        for i, ch in enumerate(s):
            value = values[ch]
            if i + 1 < len(s) and values[s[i + 1]] > value:
                total -= value
            else:
                total += value
        return total


if __name__ == "__main__":
    sol = Solution()
    assert sol.romanToInt("III") == 3
    assert sol.romanToInt("IV") == 4
    assert sol.romanToInt("IX") == 9
    assert sol.romanToInt("LVIII") == 58
    assert sol.romanToInt("MCMXCIV") == 1994
    assert sol.romanToInt("XLII") == 42
    assert sol.romanToInt("MMMCMXCIX") == 3999
    print("All self-checks passed.")
