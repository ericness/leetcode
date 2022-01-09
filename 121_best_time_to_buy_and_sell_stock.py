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
        lowest_index = 0
        lowest_value = prices[0]
        highest_index = 0
        highest_value = prices[0]

        for index, price in enumerate(prices):
            if price > highest_value:
                highest_index = index
                highest_value = price
            if price < lowest_value:
                lowest_index = index
                lowest_value = price

        return highest_value - lowest_value


# @lc code=end
