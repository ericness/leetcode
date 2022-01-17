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
        prefix_products = [1] * array_length
        suffix_products = [1] * array_length
        result = []

        for i in range(1, array_length):
            prefix_products[i] = nums[i - 1] * prefix_products[i - 1]
            suffix_i = array_length - i - 1
            suffix_products[suffix_i] = (
                nums[suffix_i + 1] * suffix_products[suffix_i + 1]
            )
        for i in range(array_length):
            result.append(prefix_products[i] * suffix_products[i])
        return result


# @lc code=end

if __name__ == "__main__":
    sol = Solution()
    answer = sol.productExceptSelf([22, 33, 44, 55])
    print(answer)
