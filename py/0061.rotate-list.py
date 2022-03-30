#
# @lc app=leetcode id=61 lang=python3
#
# [61] Rotate List
#
# https://leetcode.com/problems/rotate-list/description/
#
# algorithms
# Medium (32.38%)
# Likes:    3731
# Dislikes: 1223
# Total Accepted:    465.1K
# Total Submissions: 1.4M
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# Given the head of a linked list, rotate the list to the right by k places.
# 
# 
# Example 1:
# 
# 
# Input: head = [1,2,3,4,5], k = 2
# Output: [4,5,1,2,3]
# 
# 
# Example 2:
# 
# 
# Input: head = [0,1,2], k = 4
# Output: [2,0,1]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the list is in the range [0, 500].
# -100 <= Node.val <= 100
# 0 <= k <= 2 * 10^9
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def get_len(head):
            count = 0
            curr = ListNode(val=0, next=head)
            while curr.next:
                count += 1
                curr = curr.next
            return count, curr
        if not head:
            return None 
        list_len, last_node = get_len(head) 
        # print(list_len, last_node)
        effective_k = k % list_len
        left_k = list_len - effective_k  # left rotate num
        # form cycle
        last_node.next = head
        # cut cycle
        curr = ListNode(val=0, next=head)
        count = -1
        while curr:
            count += 1
            if count == left_k:
                new_head = curr.next
                curr.next = None
                break
            else:
                curr = curr.next
        return new_head 

# @lc code=end

