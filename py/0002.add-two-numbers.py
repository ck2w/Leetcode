#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#
# https://leetcode.com/problems/add-two-numbers/description/
#
# algorithms
# Medium (35.42%)
# Likes:    10990
# Dislikes: 2649
# Total Accepted:    1.8M
# Total Submissions: 5.1M
# Testcase Example:  '[2,4,3]\n[5,6,4]'
#
# You are given two non-empty linked lists representing two non-negative
# integers. The digits are stored in reverse order, and each of their nodes
# contains a single digit. Add the two numbers and return the sum as a linked
# list.
# 
# You may assume the two numbers do not contain any leading zero, except the
# number 0 itself.
# 
# 
# Example 1:
# 
# 
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
# 
# 
# Example 2:
# 
# 
# Input: l1 = [0], l2 = [0]
# Output: [0]
# 
# 
# Example 3:
# 
# 
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading
# zeros.
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
#     def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
#         head = ListNode()
#         curr = head
#         cum_plus = 0
#         while l1 != None and l2 != None:
#             print(l1.val, l2.val, cum_plus)
#             this_val = l1.val + l2.val + cum_plus
#             if this_val >= 10:
#                 cum_plus = 1
#                 this_val = this_val - 10
#             else:
#                 cum_plus = 0
            
#             l1 = l1.next
#             l2 = l2.next
#             curr.val = this_val
#             if l1 != None or l2 != None: 
#                 curr.next = ListNode()
#                 curr = curr.next
            

#         if l1 == None and l2 == None:
#             if cum_plus > 0:
#                 curr.next = ListNode()
#                 curr = curr.next
#                 curr.val = cum_plus
#             return head
#         elif l1 == None:
#             print(2)
#             while l2 != None or cum_plus > 0:                
#                 if l2 == None:
#                     this_val = cum_plus
#                     curr.val = this_val
#                     return head
#                 else:
#                     this_val = l2.val + cum_plus
#                 if this_val >= 10:
#                     cum_plus = 1
#                     this_val = this_val - 10
#                 else:
#                     cum_plus = 0
#                 l2 = l2.next
#                 curr.val = this_val
#                 if l2 != None or cum_plus > 0:
#                     curr.next = ListNode()
#                     curr = curr.next
#             return head
#         elif l2 == None:
#             print(3)
#             while l1 != None or cum_plus > 0:
#                 if l1 == None:
#                     this_val = cum_plus
#                     curr.val = this_val
#                     return head
#                 else:
#                     this_val = l1.val + cum_plus
#                 if this_val >= 10:
#                     cum_plus = 1
#                     this_val = this_val - 10
#                 else:
#                     cum_plus = 0
#                 l1 = l1.next
#                 curr.val = this_val
#                 if l1 != None or cum_plus > 0:
#                     curr.next = ListNode()
#                     curr = curr.next
#             return head

# 2: recursive append
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode, carry=0) -> ListNode:
        this_val = l1.val + l2.val + carry
        carry = this_val // 10
        this_val = this_val % 10
        curr = ListNode(val=this_val)

        if (l1.next != None or l2.next != None or carry > 0):
            if l1.next == None:
                l1.next = ListNode()
            if l2.next == None:
                l2.next = ListNode()
            
            curr.next = self.addTwoNumbers(l1.next, l2.next, carry)
        return curr
        

# @lc code=end

