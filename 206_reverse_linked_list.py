#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
import copy
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Reverse the order of a single linked list

        Args:
            head (Optional[ListNode]): Head node of the list

        Returns:
            Optional[ListNode]: Head node of the reversed list
        """
        if not head:
            return None
        current_node = head
        copied_node = copy.copy(head)
        copied_node.next = None
        while current_node.next:
            current_node = current_node.next
            copied_node_prev = copy.copy(current_node)
            copied_node_prev.next = copied_node
            copied_node = copied_node_prev
        return copied_node


# @lc code=end
