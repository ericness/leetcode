#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """Remove the nth from the last node.

        Args:
            head (Optional[ListNode]): Head of list
            n (int): Node to remove

        Returns:
            Optional[ListNode]: Modified list
        """
        length = 0
        current = head
        while current:
            current = current.next
            length += 1

        node_to_remove = length - n
        current = head
        for _ in range(node_to_remove - 1):
            current = current.next
        if current.next:
            current.next = current.next.next
        else:
            current.next = None

        return head


# @lc code=end

if __name__ == "__main__":
    five = ListNode(5, None)
    four = ListNode(4, five)
    three = ListNode(3, four)
    two = ListNode(2, three)
    one = ListNode(1, two)

    sol = Solution()
    result = sol.removeNthFromEnd(one, 2)
    print(result)
