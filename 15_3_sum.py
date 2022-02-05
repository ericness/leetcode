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
        nums_so_far = []
        sums = defaultdict(list)
        result = []

        for num in nums:
            if -(num) in sums:
                for two_sum in sums[-(num)]:
                    new_result = copy.deepcopy(two_sum)
                    new_result.append(num)
                    new_result = sorted(new_result)
                    if new_result not in result:
                        result.append(new_result)
            for num_so_far in nums_so_far:
                sum = num_so_far + num
                if [num_so_far, num] not in sums[sum]:
                    sums[sum].append([num_so_far, num])
            nums_so_far.append(num)
        return result


# @lc code=end

if __name__ == "__main__":
    sol = Solution()
    y = sol.threeSum([-1, 0, 1, 2, -1, -4])
    x = sol.threeSum([1, 2, 3, 4, 5, -7])
