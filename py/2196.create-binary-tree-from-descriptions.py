
# @lc app=leetcode id=2196 lang=python3
#
# [2196] 
#
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        relation_dict = dict()
        nodes_dict = dict()
        
        for line in descriptions:
            parent, child, isLeft = line
            if parent not in nodes_dict:
                node1 = TreeNode(val=parent)
                nodes_dict[parent] = node1
                
            if child not in nodes_dict:
                node2 = TreeNode(val=child)
                nodes_dict[child] = node2
            
            if isLeft:
                nodes_dict[parent].left = nodes_dict[child]
            else:
                nodes_dict[parent].right = nodes_dict[child]
            
            relation_dict[child] = parent

        while True:
            if parent in relation_dict:
                parent = relation_dict[parent]
            else:
                break
        
        return nodes_dict[parent]
# @lc code=end
