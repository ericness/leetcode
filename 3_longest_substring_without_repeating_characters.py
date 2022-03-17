#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """Count longest sequence with no repeating characters

        Args:
            s (str): String to analyze

        Returns:
            int: Length of longest sequence
        """
        left, right = 0, 0
        character_count = defaultdict(int)
        max_length = 0

        if len(s) > 0:
            character_count[s[right]] += 1

        while right < len(s):
            if all([val <= 1 for val in character_count.values()]):
                length = right - left + 1
                if length > max_length:
                    max_length = length
                right += 1
                if right < len(s):
                    character_count[s[right]] += 1
            else:
                character_count[s[left]] -= 1
                left += 1
        return max_length


# @lc code=end
