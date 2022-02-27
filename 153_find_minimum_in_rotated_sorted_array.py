#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#

# @lc code=start
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        center = len(nums) // 2
        right = len(nums) - 1

        while True:
            left_value = nums[left]
            center_value = nums[center]
            right_value = nums[right]
            if center - left <= 1 and right - center <= 1:
                return min(left_value, center_value, right_value)
            elif left_value < center_value < right_value:
                return left_value
            elif left_value > center_value:
                right = center
                center = center - (center - left) // 2
            elif center_value > right_value:
                left = center
                center = center + (right - center) // 2


# @lc code=end

if __name__ == "__main__":
    sol = Solution()
    res = sol.findMin([4, 5, 6, 7, 0, 1, 2])
    print(res)
