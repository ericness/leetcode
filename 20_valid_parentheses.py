#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
from collections import deque

MATCHES = {
    "(": ")",
    "[": "]",
    "{": "}",
}


class Solution:
    def isValid(self, s: str) -> bool:
        """Determine if parentheses are in valid order.

        Args:
            s (str): Sequence of parentheses, brackets and braces

        Returns:
            bool: Is valid sequence
        """
        paren_order = deque()
        for char in s:
            if char in MATCHES.keys():
                paren_order.append(char)
            elif char in MATCHES.values() and len(paren_order) > 0:
                open = paren_order.pop()
                if char != MATCHES[open]:
                    return False
            else:
                return False
        return len(paren_order) == 0


# @lc code=end
