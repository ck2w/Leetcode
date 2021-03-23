#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#
# https://leetcode.com/problems/validate-binary-search-tree/description/
#
# algorithms
# Medium (28.80%)
# Likes:    5620
# Dislikes: 662
# Total Accepted:    926.1K
# Total Submissions: 3.2M
# Testcase Example:  '[2,1,3]'
#
# Given the root of a binary tree, determine if it is a valid binary search
# tree (BST).
# 
# A valid BST is defined as follows:
# 
# 
# The left subtree of a node contains only nodes with keys less than the node's
# key.
# The right subtree of a node contains only nodes with keys greater than the
# node's key.
# Both the left and right subtrees must also be binary search trees.
# 
# 
# 
# Example 1:
# 
# 
# Input: root = [2,1,3]
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: root = [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [1, 10^4].
# -2^31 <= Node.val <= 2^31 - 1
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 1: min/max value bottom-up
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:       
        
        valid, _, _ =  self.check_valid(root)        
        return valid
    
    def check_valid(self, root):
        min_val = root.val
        max_val = root.val
        if root.left:
            valid, left_min_val, left_max_val = self.check_valid(root.left)
            if not valid or left_max_val >= root.val:
                return False, 0, 0
            else:
                min_val = min(min_val, left_min_val)
        if root.right:
            valid, right_min_val, right_max_val = self.check_valid(root.right)
            if not valid or right_min_val <= root.val:
                return False, 0, 0
            else:
                max_val = max(max_val, right_max_val)

        return True, min_val, max_val


# 2: min/max value top-down
import math
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        def validate(node, low=-math.inf, high=math.inf):
            # Empty trees are valid BSTs.
            if not node:
                return True
            # The current node's value must be between low and high.
            if node.val <= low or node.val >= high:
                return False

            # The left and right subtree must also be valid.
            return (validate(node.right, node.val, high) and
                   validate(node.left, low, node.val))

        return validate(root)


# @lc code=end

