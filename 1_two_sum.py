#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """Find indexes of numbers that sum to target number.

        Args:
            nums (List[int]): List of numbers to consider.
            target (int): Number to sum to.

        Raises:
            ValueError: No numbers in nums sum to target.

        Returns:
            List[int]: Indices of first and last number.
        """
        indices = {}
        for index, num in enumerate(nums):
            if target - num in indices:
                return [indices[target - num], index]
            indices[num] = index


# @lc code=end
