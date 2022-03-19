#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """Find number of islands in grid.

        Args:
            grid (List[List[str]]): Grid with 0s and 1s

        Returns:
            int: Number of islands
        """
        current_island = 2

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    mark_island(grid, row, col, str(current_island))
                    current_island += 1
        return current_island - 2


def mark_island(grid: List[List[str]], row: int, col: int, island_number: str):
    """Recursively mark all parts of an island with island_number.

    Args:
        grid (List[List[str]]): Grid with 0s and 1s
        row (int): Grid row
        col (int): Grid column
        island_number (str): Number to mark the island with
    """
    if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
        return
    elif grid[row][col] == "0":
        return
    elif grid[row][col] == "1":
        grid[row][col] = island_number
        mark_island(grid, row - 1, col, island_number)
        mark_island(grid, row, col - 1, island_number)
        mark_island(grid, row + 1, col, island_number)
        mark_island(grid, row, col + 1, island_number)
        return
    else:
        return


# @lc code=end
