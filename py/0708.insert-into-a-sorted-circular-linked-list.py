
# @lc app=leetcode id=708 lang=python3
#
# [708] Insert into a sorted Circular Linked List
#
# https://leetcode.com/problems/insert-into-a-sorted-circular-linked-list/
# Medium
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from numpy import insert


class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        # len=0
        if not head:
            node = ListNode(val=insertVal)
            node.next = node
            return node
        # len=1
        if head.next == head:
            head.next = ListNode(val=insertVal, next=head)
            return head

        slow = head
        fast = head.next
        toInsert = False
        while True:
            if (slow.val <= insertVal <= fast.val) or (insertVal <= fast.val < slow.val) or (fast.val < slow.val <= insertVal):
                slow.next = ListNode(val=insertVal, next=fast)
                break
            slow, fast = slow.next, fast.next
            # one loop end
            if slow == head:
                break
        # case: all same
        slow.next = Node(val=insertVal, next=fast)
        return head

# @lc code=end

