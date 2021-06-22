#
# @lc app=leetcode id=445 lang=python3
#
# [445] Add Two Numbers II
#
# https://leetcode.com/problems/add-two-numbers-ii/description/
#
# algorithms
# Medium (56.34%)
# Likes:    2236
# Dislikes: 198
# Total Accepted:    228.2K
# Total Submissions: 404.5K
# Testcase Example:  '[7,2,4,3]\n[5,6,4]'
#
# You are given two non-empty linked lists representing two non-negative
# integers. The most significant digit comes first and each of their nodes
# contain a single digit. Add the two numbers and return it as a linked list.
# 
# You may assume the two numbers do not contain any leading zero, except the
# number 0 itself.
# 
# Follow up:
# What if you cannot modify the input lists? In other words, reversing the
# lists is not allowed.
# 
# 
# 
# Example:
# 
# Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 8 -> 0 -> 7
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import List


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def reverse_list(head: ListNode) -> ListNode:
            prev = None
            curr = head
            while curr:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
            return prev

        l1_r = ListNode(val=0, next=reverse_list(l1))
        l2_r = ListNode(val=0, next=reverse_list(l2))

        result_head = ListNode(val=0)
        curr = result_head
        carry = 0


        while l1_r.next or l2_r.next or carry > 0:
            if not l1_r.next:
                l1_r.next = ListNode(val=0)
            if not l2_r.next:
                l2_r.next = ListNode(val=0)

            val = l1_r.next.val + l2_r.next.val + carry            
            carry = val // 10
            val = val % 10
            
            new_node = ListNode(val=val)
            curr.next = new_node
            curr = curr.next
            l1_r = l1_r.next
            l2_r = l2_r.next

        result_reverse = reverse_list(result_head.next)
        
        return result_reverse

# @lc code=end

