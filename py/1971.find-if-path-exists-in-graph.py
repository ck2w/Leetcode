#
# @lc app=leetcode id=1971 lang=python3
#
# [1971] Find if Path Exists in Graph
#
# https://leetcode.com/problems/find-if-path-exists-in-graph/description/
#
# algorithms
# Easy (49.90%)
# Likes:    579
# Dislikes: 27
# Total Accepted:    51.1K
# Total Submissions: 102.3K
# Testcase Example:  '3\n[[0,1],[1,2],[2,0]]\n0\n2'
#
# There is a bi-directional graph with n vertices, where each vertex is labeled
# from 0 to n - 1 (inclusive). The edges in the graph are represented as a 2D
# integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional
# edge between vertex ui and vertex vi. Every vertex pair is connected by at
# most one edge, and no vertex has an edge to itself.
# 
# You want to determine if there is a valid path that exists from vertex source
# to vertex destination.
# 
# Given edges and the integers n, source, and destination, return true if there
# is a valid path from source to destination, or false otherwise.
# 
# 
# Example 1:
# 
# 
# Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
# Output: true
# Explanation: There are two paths from vertex 0 to vertex 2:
# - 0 → 1 → 2
# - 0 → 2
# 
# 
# Example 2:
# 
# 
# Input: n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0,
# destination = 5
# Output: false
# Explanation: There is no path from vertex 0 to vertex 5.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 2 * 10^5
# 0 <= edges.length <= 2 * 10^5
# edges[i].length == 2
# 0 <= ui, vi <= n - 1
# ui != vi
# 0 <= source, destination <= n - 1
# There are no duplicate edges.
# There are no self edges.
# 
# 
#

# @lc code=start
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if not edges:
            return True        
        
        # use dict to store edges information, easy to find neigbors for a given node
        neighbors_dict = {}
        for edge in edges:
            node1, node2 = edge[0], edge[1]
            if node1 in neighbors_dict:
                neighbors_dict[node1].append(node2)
            else:
                neighbors_dict[node1] = [node2]
                
            if node2 in neighbors_dict:
                neighbors_dict[node2].append(node1)
            else:
                neighbors_dict[node2] = [node1]
                
        # dfs on source node
        # stack = [curr node, ...]
        stack = [source]
        visited = set()
        while stack:        
            curr_node = stack.pop()            
            for neighbor in neighbors_dict[curr_node]:
                if neighbor == destination:
                    return True
                elif neighbor in visited:                    
                    continue
                else:                    
                    stack.append(neighbor)
                    visited.add(neighbor)
        
        return False
        
# @lc code=end

