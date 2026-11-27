"""LeetCode 121 - Best Time to Buy and Sell Stock.

Given a list of daily prices, buy once and sell once afterwards to maximize
profit. If no profitable trade exists, the answer is 0.

Approach: one pass keeping the lowest price seen so far. For each day, the
best profit from selling that day is the current price minus the lowest
price before it; keep the largest such profit over all days.

Time complexity: O(n) - a single pass over the prices.
Space complexity: O(1) - only two variables are kept.
"""


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = float("inf")
        best_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > best_profit:
                best_profit = price - min_price
        return best_profit


if __name__ == "__main__":
    s = Solution()
    assert s.maxProfit([7, 1, 5, 3, 6, 4]) == 5
    assert s.maxProfit([7, 6, 4, 3, 1]) == 0
    assert s.maxProfit([1, 2]) == 1
    assert s.maxProfit([2, 1]) == 0
    assert s.maxProfit([3, 2, 6, 5, 0, 3]) == 4
    assert s.maxProfit([1]) == 0
    assert s.maxProfit([]) == 0
    assert s.maxProfit([5, 5, 5, 5]) == 0
    print("All checks passed.")
