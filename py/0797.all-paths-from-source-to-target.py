#
# @lc app=leetcode id=797 lang=python3
#
# [797] All Paths From Source to Target
#
# https://leetcode.com/problems/all-paths-from-source-to-target/description/
#
# algorithms
# Medium (80.54%)
# Likes:    3504
# Dislikes: 109
# Total Accepted:    234.6K
# Total Submissions: 291.3K
# Testcase Example:  '[[1,2],[3],[3],[]]'
#
# Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find
# all possible paths from node 0 to node n - 1 and return them in any order.
# 
# The graph is given as follows: graph[i] is a list of all nodes you can visit
# from node i (i.e., there is a directed edge from node i to node
# graph[i][j]).
# 
# 
# Example 1:
# 
# 
# Input: graph = [[1,2],[3],[3],[]]
# Output: [[0,1,3],[0,2,3]]
# Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.
# 
# 
# Example 2:
# 
# 
# Input: graph = [[4,3,1],[3,2,4],[3],[4],[]]
# Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
# 
# 
# 
# Constraints:
# 
# 
# n == graph.length
# 2 <= n <= 15
# 0 <= graph[i][j] < n
# graph[i][j] != i (i.e., there will be no self-loops).
# All the elements of graph[i] are unique.
# The input graph is guaranteed to be a DAG.
# 
# 
#

# @lc code=start
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        
        # dfs on 0 node
        # stack = [(path, visited),...]
        possible_paths = []
        stack = [([0], set([0]))]
        while stack:
            path, visited = stack.pop()
            neighbors = graph[path[-1]]
            for neighbor in neighbors:                
                if neighbor == n-1:
                    new_path = path + [neighbor]
                    possible_paths.append(new_path)
                elif neighbor in visited:
                    continue
                else:
                    new_path = path + [neighbor]
                    new_visited = visited | set([neighbor])
                    stack.append((new_path, new_visited))
        return possible_paths
# @lc code=end

