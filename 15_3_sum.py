#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#
# @lc code=start
from typing import List


class Solution:
    """Solution class for three sum"""

    def threeSum(  # pylint: disable=invalid-name
        self, nums: List[int]
    ) -> List[List[int]]:
        """Find unique triplets that sum to zero.

        Args:
            nums (List[int]): List of numbers

        Returns:
            List[List[int]]: List of triplets that sum to zero

        """
        current_index = 0
        result = []
        sorted_nums = sorted(nums)
        while current_index < len(sorted_nums) and sorted_nums[current_index] <= 0:
            current = sorted_nums[current_index]
            lower_index = current_index + 1
            upper_index = len(sorted_nums) - 1
            while lower_index < upper_index:
                lower = sorted_nums[lower_index]
                upper = sorted_nums[upper_index]
                if lower + upper + current > 0:
                    upper_index -= 1
                elif lower + upper + current < 0:
                    lower_index += 1
                else:
                    new_result = [
                        current,
                        lower,
                        upper,
                    ]
                    if new_result not in result:
                        result.append(new_result)
                    upper_index -= 1
                    lower_index += 1

            current_index += 1
        return result


# @lc code=end

if __name__ == "__main__":
    sol = Solution()
    y = sol.threeSum([-1, 0, 1, 2, -1, -4])
    print(y)
    x = sol.threeSum([1, 2, 3, 4, 5, -7])
    print(x)
