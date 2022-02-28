#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#

# @lc code=start
from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """Calculate the longer repeating character
        string when replacing with one letter

        Args:
            s (str): String to evaluate
            k (int): Number of characters to replace

        Returns:
            int: Length of longest repeating sequence
        """
        positions = defaultdict(list)
        max_length = 0

        for index, char in enumerate(s):
            positions[char].append(index)

        for indexes in positions.values():
            index_length = len(indexes)
            diffs = [
                indexes[j] - indexes[i] - 1
                for i, j in zip(range(index_length - 1), range(1, index_length))
            ]
            diffs.insert(0, indexes[0])
            diffs.append(len(s) - 1 - indexes[-1])

        return 0


# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    res = sol.characterReplacement("aabbcba", 3)
    print(res)
