#
# @lc app=leetcode id=647 lang=python3
#
# [647] Palindromic Substrings
#

# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:
        """Find number of palindromic strings in s

        Args:
            s (str): String to analyze

        Returns:
            int: Count of palindromes
        """
        palindromes = 0
        for i in range(len(s)):
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                palindromes += 1
                left -= 1
                right += 1
            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                palindromes += 1
                left -= 1
                right += 1
        return palindromes


# @lc code=end
