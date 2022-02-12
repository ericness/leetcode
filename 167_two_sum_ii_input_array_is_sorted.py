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
        for base_index, base_value in enumerate(numbers):
            search_index = self.search_value(
                numbers[base_index + 1 :], target - base_value
            )
            if search_index >= 0:
                return [base_index + 1, base_index + search_index + 2]
        raise ValueError("No solution found")

    def search_value(self, numbers: List[int], value: int) -> int:
        """Find the index of `value` in `numbers`. Otherwise
        return -1.

        Args:
            numbers (List[int]): Array of numbers to search
            value (int): Value to search for

        Returns:
            int: Index of value
        """
        lower_bound = 0
        upper_bound = len(numbers) - 1

        while upper_bound >= lower_bound:
            midpoint = (upper_bound + lower_bound) // 2
            value_at_midpoint = numbers[midpoint]

            if value_at_midpoint > value:
                upper_bound = midpoint - 1
            elif value_at_midpoint < value:
                lower_bound = midpoint + 1
            else:
                return midpoint
        return -1


# @lc code=end

if __name__ == "__main__":
    sol = Solution()
    # x = sol.search_value([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 8)
    y = sol.twoSum([0, 0, 0, 0, 0, 0, 2, 3, 9, 9, 9, 9, 9, 9], 5)
    print(y)
