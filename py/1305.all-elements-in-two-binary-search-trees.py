#
# @lc app=leetcode id=1305 lang=python3
#
# [1305] All Elements in Two Binary Search Trees
#
# https://leetcode.com/problems/all-elements-in-two-binary-search-trees/description/
#
# algorithms
# Medium (78.63%)
# Likes:    1498
# Dislikes: 49
# Total Accepted:    118.2K
# Total Submissions: 150K
# Testcase Example:  '[2,1,4]\n[1,0,3]'
#
# Given two binary search trees root1 and root2, return a list containing all
# the integers from both trees sorted in ascending order.
# 
# 
# Example 1:
# 
# 
# Input: root1 = [2,1,4], root2 = [1,0,3]
# Output: [0,1,1,2,3,4]
# 
# 
# Example 2:
# 
# 
# Input: root1 = [1,null,8], root2 = [8,1]
# Output: [1,1,8,8]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in each tree is in the range [0, 5000].
# -10^5 <= Node.val <= 10^5
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
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        # get inorder traversal
        val1 = self.inorder(root1)
        val2 = self.inorder(root2)
        result = []
                
        # merge list
        while val1 and val2:
            if val1[-1] < val2[-1]:
                result.append(val2.pop())
            else:
                result.append(val1.pop())
        while val1:
            result.append(val1.pop())
        while val2:
            result.append(val2.pop())
        return result[::-1]
    
    def inorder(self, r: TreeNode):
        return self.inorder(r.left) + [r.val] + self.inorder(r.right) if r else []
    
# @lc code=end
   