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
        lowest_price = None
        highest_price = None

        for price in prices:
            if lowest_price is None or price < lowest_price:
                lowest_price = price
                highest_price = price
            if highest_price is None or price > highest_price:
                highest_price = price
                if highest_price - lowest_price > max_profit:
                    max_profit = highest_price - lowest_price

        return max_profit


# @lc code=end
