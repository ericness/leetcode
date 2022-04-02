#
# @lc app=leetcode id=417 lang=python3
#
# [417] Pacific Atlantic Water Flow
#

# @lc code=start
from enum import Enum
from typing import List, Set, Tuple


class Ocean(str, Enum):
    ATLANTIC = "Atlantic"
    PACIFIC = "Pacific"


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        result = []
        for row in range(len(heights)):
            for col in range(len(heights[0])):
                if self.depth_first_search(
                    heights, row, col, Ocean.ATLANTIC, set()
                ) and self.depth_first_search(heights, row, col, Ocean.PACIFIC, set()):
                    result.append([row, col])

        return result

    def depth_first_search(
        self,
        heights: List[List[int]],
        row: int,
        col: int,
        ocean: Ocean,
        visited: Set[Tuple],
    ) -> bool:
        if (row, col) in visited:
            return False
        if ocean == Ocean.PACIFIC:
            if row == 0 or col == 0:
                return True
        elif ocean == Ocean.ATLANTIC:
            if row == len(heights) - 1 or col == len(heights[0]) - 1:
                return True

        visited.add((row, col))

        up, down, left, right = False, False, False, False
        if row > 0 and heights[row - 1][col] <= heights[row][col]:
            up = self.depth_first_search(heights, row - 1, col, ocean, visited)
        if row < len(heights) - 1 and heights[row + 1][col] <= heights[row][col]:
            down = self.depth_first_search(heights, row + 1, col, ocean, visited)
        if col > 0 and heights[row][col - 1] <= heights[row][col]:
            left = self.depth_first_search(heights, row, col - 1, ocean, visited)
        if col < len(heights[0]) - 1 and heights[row][col + 1] <= heights[row][col]:
            right = self.depth_first_search(heights, row, col + 1, ocean, visited)

        return any([up, down, left, right])


# @lc code=end
