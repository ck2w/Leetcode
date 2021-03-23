#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
#
# algorithms
# Medium (35.76%)
# Likes:    4908
# Dislikes: 291
# Total Accepted:    814.2K
# Total Submissions: 2.3M
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# Given the head of a linked list, remove the n^th node from the end of the
# list and return its head.
# 
# Follow up: Could you do this in one pass?
# 
# 
# Example 1:
# 
# 
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
# 
# 
# Example 2:
# 
# 
# Input: head = [1], n = 1
# Output: []
# 
# 
# Example 3:
# 
# 
# Input: head = [1,2], n = 1
# Output: [1]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 1: stack
# class Solution:
#     def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
#         stack = []
#         new_head = ListNode(next=head)
#         curr = new_head
#         while curr.next:
#             stack.append(curr)
#             curr = curr.next
        
#         for i in range(n-1):
#             stack.pop()
        
#         if stack:
#             stack[-1].next = stack[-1].next.next
#         return new_head.next

# 2: two pointers, iterate once
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        new_head = ListNode(next=head)
        first = new_head
        second = new_head

        for i in range(n+1):
            first = first.next
        
        while first:
            first = first.next
            second = second.next
        
        second.next = second.next.next

        return new_head.next
        
        
# @lc code=end

