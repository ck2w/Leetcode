#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#
# https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/
#
# algorithms
# Easy (45.71%)
# Likes:    1815
# Dislikes: 121
# Total Accepted:    498.6K
# Total Submissions: 1.1M
# Testcase Example:  '[1,1,2]'
#
# Given a sorted linked list, delete all duplicates such that each element
# appear only once.
# 
# Example 1:
# 
# 
# Input: 1->1->2
# Output: 1->2
# 
# 
# Example 2:
# 
# 
# Input: 1->1->2->3->3
# Output: 1->2->3
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# class Solution:
#     def deleteDuplicates(self, head: ListNode) -> ListNode:
#         if head == None:
#             return head
        
#         current = head.next
#         prev = head
        
#         while current != None:
#             if current.val == prev.val:
#                 prev.next = current.next
#                 current = current.next
#             else:
#                 current = current.next
#                 prev = prev.next
        
#         return head


# unordered list
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        curr = head
        while curr:
            if curr.next and curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head
# @lc code=end

