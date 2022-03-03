#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#

# @lc code=start
from collections import defaultdict
from typing import List


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

    def calculate_length(self, diffs: List[int], k: int) -> int:
        """Calculate maximum sequence length based
        on the differences between character positions

        Args:
            diffs (List[int]): List of position differences
            k (int): Number of characters to replace

        Returns:
            int: Maximum length of replacement
        """
        behind, ahead = 0, 0
        current_k = diffs[0]
        max_length = 0

        while ahead < len(diffs):
            if current_k <= k:
                ahead += 1
                if ahead == len(diffs):
                    break
                current_k += diffs[ahead]
            else:
                behind += 1
                current_k -= diffs[behind]
            length = ahead - behind + current_k
            if length > max_length and current_k <= k:
                max_length = length

        return max_length


# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    # res = sol.characterReplacement("aabbcba", 3)
    res = sol.calculate_length([1, 2, 1], 2)
    print(res)
