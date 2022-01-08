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

        prev_node = head
        if prev_node.next:
            current_node = prev_node.next
            prev_node.next = None
            if current_node.next:
                next_node = current_node.next
            # two nodes in list
            else:
                next_node = None
        # one node in list
        else:
            return prev_node

        while next_node:
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
            next_node = next_node.next

        current_node.next = prev_node
        return current_node


# @lc code=end

if __name__ == "__main__":
    five = ListNode(5, None)
    four = ListNode(4, five)
    three = ListNode(3, four)
    two = ListNode(2, three)
    one = ListNode(1, two)

    solution = Solution()
    result = solution.reverseList(one)
    print(result)
