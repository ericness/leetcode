#
# @lc app=leetcode id=572 lang=python3
#
# [572] Subtree of Another Tree
#

# @lc code=start
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        elif self.areTreesEqual(root, subRoot):
            return True
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(
                root.right, subRoot
            )

    def areTreesEqual(
        self, root1: Optional[TreeNode], root2: Optional[TreeNode]
    ) -> bool:
        if root1 is None and root2 is None:
            return True
        elif root1 and root2 and root1.val == root2.val:
            return self.areTreesEqual(root1.left, root2.left) and self.areTreesEqual(
                root1.right, root2.right
            )
        else:
            return False


# @lc code=end
