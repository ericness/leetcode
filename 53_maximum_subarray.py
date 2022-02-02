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
        current = 0
        max_sum = -10001

        for num in nums:
            if current < 0:
                current = 0
            current += num
            if current > max_sum:
                max_sum = current

        return max_sum


# @lc code=end

if __name__ == "__main__":
    sol = Solution()
    result = sol.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    result = sol.maxSubArray([-3, -2, -1])
    result = sol.maxSubArray([1, 1, -10, 2, 2])
    result = sol.maxSubArray([7, 8, -1, 9, 10])
    result = sol.maxSubArray([-4, -3, -2, -1])
    print(result)
