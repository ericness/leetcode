#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#
# @lc code=start

import copy
from collections import defaultdict
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """Find unique triplets that sum to zero.

        Args:
            nums (List[int]): List of numbers

        Returns:
            List[List[int]]: List of triplets that sum to zero

        """
        result = []
        for i in range(len(nums)):
            nums_set = set()
            for j in range(i + 1, len(nums)):
                if -(nums[i] + nums[j]) in nums_set:
                    new_result = sorted(
                        [
                            nums[i],
                            nums[j],
                            -(nums[i] + nums[j]),
                        ]
                    )
                    if new_result not in result:
                        result.append(new_result)
                else:
                    nums_set.add(nums[j])

        return result


# @lc code=end

if __name__ == "__main__":
    sol = Solution()
    y = sol.threeSum([-1, 0, 1, 2, -1, -4])
    x = sol.threeSum([1, 2, 3, 4, 5, -7])
