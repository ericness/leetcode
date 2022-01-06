#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """Check if nums has duplicate elements.

        Args:
            nums (List[int]): List of ints

        Returns:
            bool: Does nums contain duplicates
        """
        return len(nums) > len(set(nums))

# @lc code=end
