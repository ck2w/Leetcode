#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#
# https://leetcode.com/problems/palindrome-linked-list/description/
#
# algorithms
# Easy (40.43%)
# Likes:    4733
# Dislikes: 428
# Total Accepted:    567.4K
# Total Submissions: 1.4M
# Testcase Example:  '[1,2]'
#
# Given a singly linked list, determine if it is a palindrome.
# 
# Example 1:
# 
# 
# Input: 1->2
# Output: false
# 
# Example 2:
# 
# 
# Input: 1->2->2->1
# Output: true
# 
# Follow up:
# Could you do it in O(n) time and O(1) space?
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        curr = head
        length = 0

        # get length
        while curr:
            length = length + 1
            curr = curr.next
               
        # stack
        lst = []
        count = 0
        curr = head
        while curr:
            # ignore mid point for odd length
            if length % 2 == 1 and count == length // 2:
                curr = curr.next

            if count < length // 2:
                # left half, push to stack
                lst.append(curr.val)
                curr = curr.next
            else:
                # right half, pop if match
                if not lst:  return True
                if curr.val == lst[-1]:
                    lst.pop()                    
                else:
                    return False
                curr = curr.next
            count = count + 1
        return True

       
# @lc code=end

