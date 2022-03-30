#
# @lc app=leetcode id=547 lang=python3
#
# [547] Number of Provinces
#
# https://leetcode.com/problems/number-of-provinces/description/
#
# algorithms
# Medium (62.44%)
# Likes:    4478
# Dislikes: 218
# Total Accepted:    398.6K
# Total Submissions: 638.2K
# Testcase Example:  '[[1,1,0],[1,1,0],[0,0,1]]'
#
# There are n cities. Some of them are connected, while some are not. If city a
# is connected directly with city b, and city b is connected directly with city
# c, then city a is connected indirectly with city c.
# 
# A province is a group of directly or indirectly connected cities and no other
# cities outside of the group.
# 
# You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the
# i^th city and the j^th city are directly connected, and isConnected[i][j] = 0
# otherwise.
# 
# Return the total number of provinces.
# 
# 
# Example 1:
# 
# 
# Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
# Output: 3
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 200
# n == isConnected.length
# n == isConnected[i].length
# isConnected[i][j] is 1 or 0.
# isConnected[i][i] == 1
# isConnected[i][j] == isConnected[j][i]
# 
# 
#

# @lc code=start
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        # use dict to store edges information, easy to find neigbors for a given node
        neighbors_dict = {k: [] for k in range(n)}
        for i in range(n):
            for j in range(i, n):
                if isConnected[i][j] == 1:                
                    neighbors_dict[i].append(j)
                    neighbors_dict[j].append(i)
        
        visited = set()        
        count = 0
        
        for node in range(n):
            # check if curr node is in new component
            if node not in visited:
                count += 1
            else:
                continue
            
            # new component: notate all connected nodes to visited
            # dfs
            stack = [node]
            while stack:
                curr_node = stack.pop()
                neighbors = neighbors_dict[curr_node]
                for neighbor in neighbors:
                    if neighbor not in visited:                        
                        visited.add(neighbor)
                        stack.append(neighbor)
            
        return count
# @lc code=end

