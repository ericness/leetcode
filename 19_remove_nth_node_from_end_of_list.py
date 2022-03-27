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
        dummy = ListNode(0, head)
        left = dummy
        right = head

        node_index = 0
        while node_index < n:
            right = right.next
            node_index += 1

        while right:
            right = right.next
            left = left.next

        left.next = left.next.next

        return dummy.next


# @lc code=end

if __name__ == "__main__":
    five = ListNode(5, None)
    four = ListNode(4, five)
    three = ListNode(3, four)
    two = ListNode(2, three)
    one = ListNode(1, two)
    # one = ListNode(1, None)

    sol = Solution()
    result = sol.removeNthFromEnd(one, 1)
    print(result)
