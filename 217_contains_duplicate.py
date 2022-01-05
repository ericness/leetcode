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
        if not nums:
            return False
        collection = collections.Counter(nums)
        return collection.most_common(1)[0][1] > 1 

# @lc code=end

if __name__ == "__main__":
    sol = Solution()
    print(sol.containsDuplicate([1, 2, 3, 1]))
