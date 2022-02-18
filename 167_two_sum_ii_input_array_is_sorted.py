#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
from typing import List


class Solution:
    """Solution class for Two Sum"""

    def twoSum(  # pylint: disable=invalid-name
        self, numbers: List[int], target: int
    ) -> List[int]:
        """Find the indices of the two numbers that add to target.

        Args:
            numbers (List[int]): Sorted list of ints
            target (int): Target to sum to

        Returns:
            List[int]: List of two indices added by one
        """
        lower_index = 0
        upper_index = len(numbers) - 1

        while lower_index < upper_index:
            lower_value = numbers[lower_index]
            upper_value = numbers[upper_index]
            lower_upper_sum = lower_value + upper_value
            if lower_upper_sum == target:
                return [lower_index + 1, upper_index + 1]
            elif lower_upper_sum < target:
                lower_index += 1
            else:
                upper_index -= 1
        raise ValueError("No solution found")


# @lc code=end

if __name__ == "__main__":
    sol = Solution()
    # x = sol.search_value([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 8)
    y = sol.twoSum([0, 0, 0, 0, 0, 0, 2, 3, 9, 9, 9, 9, 9, 9], 5)
    print(y)
