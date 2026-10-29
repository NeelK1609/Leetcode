class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        prefix = strs[0]
        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix


if __name__ == "__main__":
    sol = Solution()
    assert sol.longestCommonPrefix(["flower", "flow", "flight"]) == "fl"
    assert sol.longestCommonPrefix(["dog", "racecar", "car"]) == ""
    assert sol.longestCommonPrefix(["interspecies", "interstellar", "interstate"]) == "inters"
    assert sol.longestCommonPrefix(["a"]) == "a"
    assert sol.longestCommonPrefix(["", "b"]) == ""
    assert sol.longestCommonPrefix(["ab", "a"]) == "a"
    assert sol.longestCommonPrefix(["cir", "car"]) == "c"
    print("All 7 checks passed.")
