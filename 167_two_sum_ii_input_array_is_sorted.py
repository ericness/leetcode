#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """Find the indices of the two numbers that add to target.

        Args:
            numbers (List[int]): Sorted list of ints
            target (int): Target to sum to

        Returns:
            List[int]: List of two indices added by one
        """
        for base_index in range(len(numbers)):
            search_index = self.search_value(
                numbers[base_index + 1 :], target - numbers[base_index]
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
        current = (len(numbers) - 1) // 2
        level = 0
        while len(numbers) >= 2 ** level:
            level += 1
            if numbers[current] < value:
                current = current + max(len(numbers) // 2 ** (level + 1), 1)
            elif numbers[current] > value:
                current = current - max(len(numbers) // 2 ** (level + 1), 1)
            else:
                return current
        return -1


# @lc code=end

if __name__ == "__main__":
    sol = Solution()
    # x = sol.search_value([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 8)
    y = sol.twoSum([0, 0, 0, 0, 0, 1, 1], 2)
    print(y)
