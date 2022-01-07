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
        nodes = []
        current_node = head
        while current_node.next:
            nodes.append(copy.copy(current_node))
            current_node = current_node.next
        nodes.append(current_node)
        nodes.reverse()
        for index, node in enumerate(nodes):
            next_index = index + 1
            if next_index < len(nodes):
                node.next = nodes[next_index]
            else:
                node.next = None
        return nodes[0]


# @lc code=end
