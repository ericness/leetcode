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

DIRECTIONS = [
    Direction(-1, 0),
    Direction(1, 0),
    Direction(0, -1),
    Direction(0, 1),
]


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
                node = Node(row, col)
                if grid[node.row][node.col] == "1":
                    breadth_first_search(grid, visited, node)
                    number_islands += 1
        return number_islands


def breadth_first_search(
    grid: List[List[str]], visited: Set[Tuple[int, int]], node: Node
) -> Set[Tuple[int, int]]:
    """Perform breadth first search on specified grid element

    Args:
        grid (List[List[str]]): Grid with 0s and 1s
        visited (Set[Tuple[int, int]]): Set of visited nodes
        node (Node): Node to search
    Returns:
        Set[Tuple[int, int]]: Set of nodes visited by function
    """
    row_count = len(grid)
    col_count = len(grid[0])
    local_visited = set()
    node_queue = collections.deque()
    node_queue.append(node)

    while node_queue:
        search_node = node_queue.popleft()
        for direction in DIRECTIONS:
            new_node = Node(
                search_node.row + direction.rows_down,
                search_node.col + direction.cols_right,
            )

            if (
                0 < new_node.row < row_count
                and 0 < new_node.col < col_count
                and new_node not in visited
                and new_node not in local_visited
                and grid[new_node.row][new_node.col] == "1"
            ):
                node_queue.append(new_node)
            local_visited.add(new_node)
    return local_visited


# @lc code=end
