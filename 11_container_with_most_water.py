#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """Calculate max area between array elements.

        Args:
            height (List[int]): List of heights

        Returns:
            int: Max area for water
        """
        left = 0
        right = len(height) - 1
        max_area = 0
        while left < right:
            area = min(height[left], height[right]) * (right - left)
            if area > max_area:
                max_area = area
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return max_area


# @lc code=end
