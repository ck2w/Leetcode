#
# @lc app=leetcode id=138 lang=python3
#
# [138] Copy List with Random Pointer
#
# https://leetcode.com/problems/copy-list-with-random-pointer/description/
#
# algorithms
# Medium (41.00%)
# Likes:    4895
# Dislikes: 804
# Total Accepted:    546.7K
# Total Submissions: 1.3M
# Testcase Example:  '[[7,null],[13,0],[11,4],[10,2],[1,0]]'
#
# A linked list of length n is given such that each node contains an additional
# random pointer, which could point to any node in the list, or null.
# 
# Construct a deep copy of the list. The deep copy should consist of exactly n
# brand new nodes, where each new node has its value set to the value of its
# corresponding original node. Both the next and random pointer of the new
# nodes should point to new nodes in the copied list such that the pointers in
# the original list and copied list represent the same list state. None of the
# pointers in the new list should point to nodes in the original list.
# 
# For example, if there are two nodes X and Y in the original list, where
# X.random --> Y, then for the corresponding two nodes x and y in the copied
# list, x.random --> y.
# 
# Return the head of the copied linked list.
# 
# The linked list is represented in the input/output as a list of n nodes. Each
# node is represented as a pair of [val, random_index] where:
# 
# 
# val: an integer representing Node.val
# random_index: the index of the node (range from 0 to n-1) that the random
# pointer points to, or null if it does not point to any node.
# 
# 
# Your code will only be given the head of the original linked list.
# 
# 
# Example 1:
# 
# 
# Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
# Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
# 
# 
# Example 2:
# 
# 
# Input: head = [[1,1],[2,1]]
# Output: [[1,1],[2,1]]
# 
# 
# Example 3:
# 
# 
# 
# 
# Input: head = [[3,null],[3,0],[3,null]]
# Output: [[3,null],[3,0],[3,null]]
# 
# 
# Example 4:
# 
# 
# Input: head = []
# Output: []
# Explanation: The given linked list is empty (null pointer), so return
# null.
# 
# 
# 
# Constraints:
# 
# 
# 0 <= n <= 1000
# -10000 <= Node.val <= 10000
# Node.random is null or is pointing to some node in the linked list.
# 
# 
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

# Time: O(N), Space: O(1)
# class Solution:
#     def copyRandomList(self, head: 'Node') -> 'Node':
#         # list len=0
#         if not head:
#             return None
        
#         # list len=1
#         if not head.next:
#             new_head = Node(x=head.val)
#             if head.random:
#                 new_head.random = new_head
#             return new_head

#         curr = head
#         # create and merge copy list
#         while curr:
#             new_node = Node(x=curr.val)            
#             new_node.next = curr.next
#             curr.next = new_node
#             curr = new_node.next            

#         # copy random pointer
#         curr = head
#         while curr:            
#             if curr.random:
#                 curr.next.random = curr.random.next            
#             curr = curr.next.next

#         # seperate copy list
#         new_head = head.next
#         curr = new_head
#         while curr:
#             curr.next = curr.next.next
#             if curr.next.next:
#                 curr = curr.next
#             else:
#                 break
#         return new_head

# Time: O(n)
# visited_nodes: 
# # key: old node, value: new node
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        visited_nodes = {}

        def build_list(node: Node) -> Node:
            if not node: 
                return None
            nonlocal visited_nodes
            if node in visited_nodes: 
                return visited_nodes[node]
            visited_nodes[node] = Node(x=node.val)
            visited_nodes[node].next = build_list(node.next)
            visited_nodes[node].random = build_list(node.random)
            return visited_nodes[node]

        return build_list(head)

# @lc code=end

