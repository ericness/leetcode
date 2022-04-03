#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        left, right = 0, 0
        while right < len(prices):
            if prices[right] - prices[left] > max_profit:
                max_profit = prices[right] - prices[left]
            if prices[right] < prices[left]:
                left = right
            right += 1
        return max_profit


# @lc code=end
