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
            for j in range(i, len(s)):
                if s[i:j] == s[j:i:-1]:
                    palindromes += 1
        return palindromes


# @lc code=end
