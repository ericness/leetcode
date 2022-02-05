#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """Find unique triplets that sum to zero.

        Args:
            nums (List[int]): List of numbers

        Returns:
            List[List[int]]: List of triplets that sum to zero

        """
        nums_map = {num: index for index, num in enumerate(nums)}
        result = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                negative_sum = -(nums[i] + nums[j])
                if negative_sum in nums_map and nums_map[negative_sum] not in [i, j]:
                    triplet = sorted([nums[i], nums[j], negative_sum])
                    if triplet not in result:
                        result.append(triplet)
        return result


# @lc code=end
