#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
from collections import defaultdict
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    """Node in a linked list"""

    def __init__(self, x):
        self.val = x
        self.next: Optional[ListNode] = None


class Solution:
    """LeetCode solution"""

    def hasCycle(  # pylint: disable=invalid-name
        self, head: Optional[ListNode]
    ) -> bool:
        """Determine if a linked list has a cycle

        Args:
            head (Optional[ListNode]): First node of list

        Returns:
            bool: True if there is a cycle
        """
        if not head:
            return False
        current = head
        seen_nodes = defaultdict(list)

        while current.next:
            for node in seen_nodes.get(current.val, []):
                if current is node:
                    return True
            seen_nodes[current.val].append(current)
            current = current.next
        return False


# @lc code=end
if __name__ == "__main__":
    one = ListNode(3)
    two = ListNode(2)
    three = ListNode(0)
    four = ListNode(-4)
    one.next = two
    two.next = three
    three.next = four
    four.next = two
    sol = Solution()
    result = sol.hasCycle(one)
    print(result)
