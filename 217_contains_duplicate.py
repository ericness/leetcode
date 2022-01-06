#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
import collections
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        previous_nums = set()
        for num in nums:
            if num in previous_nums:
                return True
            previous_nums.add(num)
        return False

# @lc code=end

if __name__ == "__main__":
    sol = Solution()
    print(sol.containsDuplicate([1, 2, 3, 1]))
