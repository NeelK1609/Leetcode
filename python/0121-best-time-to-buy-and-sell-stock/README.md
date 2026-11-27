# LeetCode 121 - Best Time to Buy and Sell Stock

**Difficulty:** Easy

## Problem

You are given the price of a stock on each day. You may buy one share on one
day and sell it on a later day. Find the largest profit you can make, or 0 if
no buy-then-sell trade is profitable.

## Approach

Scan the prices once, remembering the lowest price seen so far. For each day,
the best profit from selling that day is the current price minus that lowest
earlier price. Keep the largest such profit across all days.

## Complexity

- Time: O(n) - a single pass over the prices.
- Space: O(1) - only the lowest price and the best profit are stored.
