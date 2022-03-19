#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
import collections
from enum import Enum
from typing import List, Set, Tuple

Node = collections.namedtuple("Node", "row col")
Direction = collections.namedtuple("Direction", "rows_down cols_right")


class Directions(Enum):
    Up = Direction(-1, 0)
    Down = Direction(1, 0)
    Left = Direction(0, -1)
    Right = Direction(0, 1)


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """Find number of islands in grid.

        Args:
            grid (List[List[str]]): Grid with 0s and 1s

        Returns:
            int: Number of islands
        """
        row_count = len(grid)
        col_count = len(grid[0])
        visited = set()
        number_islands = 0

        for row in range(row_count):
            for col in range(col_count):
                if grid[row][col] == "1":
                    mark_island(grid, row, col, str(current_island))
                    current_island += 1
        return number_islands


def breadth_first_search(
    grid: List[List[str]], visited: Set[Tuple[int, int]], row: int, col: int
) -> Set[Tuple[int, int]]:
    """Perform breadth first search on specified grid element

    Args:
        grid (List[List[str]]): Grid with 0s and 1s
        visited (Set[Tuple[int, int]]): Set of visited nodes
        row (int): Grid row
        col (int): Grid column
    Returns:
        Set[Tuple[int, int]]: Set of nodes visited by function
    """
    node_queue = collections.deque()
    node_queue.append((row, col))

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
