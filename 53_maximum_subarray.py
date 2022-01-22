#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        max_sum = -10001
        for i in range(len(nums)):
            for j in range(len(nums)):
                if j > i:
                    subarray_sum = sum(nums[i:j])
                    if subarray_sum > max_sum:
                        max_sum = subarray_sum
        return max_sum


# @lc code=end
