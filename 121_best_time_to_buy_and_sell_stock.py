#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """Calculate maximum profit.

        Args:
            prices (List[int]): List of daily prices

        Returns:
            int: Maximum profit
        """
        max_profit = 0

        for low_index, low_price in enumerate(prices):
            for high_index, high_price in enumerate(prices):
                if high_index > low_index and high_price - low_price > max_profit:
                    max_profit = high_price - low_price

        return max_profit


# @lc code=end
