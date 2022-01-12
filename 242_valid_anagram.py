#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """Determine if a word is an anagram.

        Args:
            s (str): Base word
            t (str): Potential anagram

        Returns:
            bool: Is valid anagram
        """
        return Counter(s) == Counter(t)


# @lc code=end
