"""LeetCode 20: Valid Parentheses.

Approach: scan the string left to right, pushing each opening bracket
onto a stack. For each closing bracket, check that the top of the stack
holds the matching opener; if it doesn't (or the stack is empty), the
string is invalid. At the end, the string is valid only if the stack
is empty, meaning every opener was closed in the right order.

Time complexity: O(n), one pass over the string.
Space complexity: O(n) in the worst case (all opening brackets).
"""


class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {")": "(", "]": "[", "}": "{"}
        stack: list[str] = []
        for ch in s:
            if ch in pairs:
                if not stack or stack.pop() != pairs[ch]:
                    return False
            else:
                stack.append(ch)
        return not stack


if __name__ == "__main__":
    sol = Solution()
    assert sol.isValid("()") is True
    assert sol.isValid("()[]{}") is True
    assert sol.isValid("(]") is False
    assert sol.isValid("([)]") is False
    assert sol.isValid("{[]}") is True
    assert sol.isValid("") is True
    assert sol.isValid("(") is False
    assert sol.isValid(")") is False
    assert sol.isValid("((()))") is True
    print("All self-checks passed.")
