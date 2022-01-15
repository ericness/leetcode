#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """Calculate an array of the products for every element
        in the array except the one at the same index.

        Args:
            nums (List[int]): Array of ints

        Returns:
            List[int]: Array of products
        """
        result = []
        for i in range(len(nums)):
            prefix_product = 1
            suffix_product = 1
            for pre in nums[:i]:
                prefix_product *= pre
            for suf in nums[i + 1 :]:
                suffix_product *= suf
            result.append(prefix_product * suffix_product)
        return result


# @lc code=end
