class Solution:
    def climbStairs(self, n: int) -> int:
        # Ways to reach step n = ways to reach n-1 (one step) + ways to
        # reach n-2 (two steps): the Fibonacci recurrence, kept O(1) space.
        if n <= 2:
            return n
        prev, curr = 1, 2
        for _ in range(3, n + 1):
            prev, curr = curr, prev + curr
        return curr


if __name__ == "__main__":
    sol = Solution()
    # LeetCode 70 examples + edge cases.
    assert sol.climbStairs(1) == 1
    assert sol.climbStairs(2) == 2
    assert sol.climbStairs(3) == 3
    assert sol.climbStairs(4) == 5
    assert sol.climbStairs(5) == 8
    assert sol.climbStairs(10) == 89
    assert sol.climbStairs(20) == 10946
    assert sol.climbStairs(45) == 1836311903
    print("All 8 checks passed.")
