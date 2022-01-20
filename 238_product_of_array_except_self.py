#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """Calculate an array of the products for every element
        in the array except the one at the same index.

        Args:
            nums (List[int]): Array of ints

        Returns:
            List[int]: Array of products
        """
        array_length = len(nums)
        prefix = 1
        suffix = 1
        result = [1] * array_length

        for i in range(1, array_length):
            prefix *= nums[i - 1]
            result[i] *= prefix

            suffix_i = array_length - i - 1
            suffix *= nums[suffix_i + 1]
            result[suffix_i] *= suffix

        return result


# @lc code=end
