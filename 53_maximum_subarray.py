#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """Find subarray with largest sum

        Args:
            nums (List[int]): Array of numbers

        Returns:
            int: Sum of max subarray
        """
        array_size = len(nums)
        left_current = 0
        left_min = -10001
        left_index = 0
        right_current = 0
        right_min = -10001
        right_index = 0
        for i in range(array_size):
            if nums[i] + left_current > left_min:
                left_max = left_current + nums[i]
                left_index = i

            left_current += nums[i]

        for i in range(array_size):
            j = array_size - i - 1
            if nums[j] + left_current > left_max:
                left_max = left_current + nums[j]
                left_index = j

            left_current += nums[j]

        return right_max - left_max


# @lc code=end

if __name__ == "__main__":
    sol = Solution()
    result = sol.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    result = sol.maxSubArray([1, 1, -10, 2, 2])
    # result = sol.maxSubArray([-4, -3, -2, -1])
    print(result)
