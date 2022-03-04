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
            if char not in positions.keys():
                positions[char] = [0] * len(s)
            positions[char][index] = 1

        for char_array in positions.values():
            char_length = self.calculate_length(char_array, k)
            if char_length > max_length:
                max_length = char_length

        return max_length

    def calculate_length(self, char_positions: List[int], k: int) -> int:
        """Calculate maximum sequence length based
        on the character positions

        Args:
            diffs (List[int]): List of character position
            k (int): Number of characters to replace

        Returns:
            int: Maximum length of replacement
        """
        behind, ahead = 0, 0
        match_count = 1 if char_positions[0] == 1 else 0
        nonmatch_count = 1 if char_positions[0] == 0 else 0
        max_length = 0

        while ahead < len(char_positions):
            if nonmatch_count <= k:
                ahead += 1
                if ahead == len(char_positions):
                    break
                if char_positions[ahead] == 1:
                    match_count += 1
                else:
                    nonmatch_count += 1
            else:
                if char_positions[behind] == 1:
                    match_count -= 1
                else:
                    nonmatch_count -= 1
                behind += 1
            length = match_count + nonmatch_count
            if length > max_length and nonmatch_count <= k:
                max_length = length

        return max_length


# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    # res = sol.characterReplacement("aabbcba", 3)
    res = sol.calculate_length([1, 1, 0, 1, 0, 0, 1], 1)
    print(res)
