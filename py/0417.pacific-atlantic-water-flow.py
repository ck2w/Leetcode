#
# @lc app=leetcode id=417 lang=python3
#
# [417] Pacific Atlantic Water Flow
#
# https://leetcode.com/problems/pacific-atlantic-water-flow/description/
#
# algorithms
# Medium (42.64%)
# Likes:    1833
# Dislikes: 436
# Total Accepted:    103.8K
# Total Submissions: 242.4K
# Testcase Example:  '[[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]'
#
# Given an m x n matrix of non-negative integers representing the height of
# each unit cell in a continent, the "Pacific ocean" touches the left and top
# edges of the matrix and the "Atlantic ocean" touches the right and bottom
# edges.
# 
# Water can only flow in four directions (up, down, left, or right) from a cell
# to another one with height equal or lower.
# 
# Find the list of grid coordinates where water can flow to both the Pacific
# and Atlantic ocean.
# 
# Note:
# 
# 
# The order of returned grid coordinates does not matter.
# Both m and n are less than 150.
# 
# 
# 
# 
# Example:
# 
# 
# Given the following 5x5 matrix:
# 
# ⁠ Pacific ~   ~   ~   ~   ~ 
# ⁠      ~  1   2   2   3  (5) *
# ⁠      ~  3   2   3  (4) (4) *
# ⁠      ~  2   4  (5)  3   1  *
# ⁠      ~ (6) (7)  1   4   5  *
# ⁠      ~ (5)  1   1   2   4  *
# ⁠         *   *   *   *   * Atlantic
# 
# Return:
# 
# [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with
# parentheses in above matrix).
# 
# 


# @lc code=start
class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or not matrix[0]: 
            return []
        m = len(matrix)
        n = len(matrix[0])
        
        from collections import deque

        pacific_queue = deque()
        atlantic_queue = deque()

        for i in range(m):
            pacific_queue.append((i, 0))
            atlantic_queue.append((i, n-1))

        for i in range(n):
            pacific_queue.append((0, i))
            atlantic_queue.append((m-1, i))
        
        def dfs(queue):
            reachable = set()
            checked = set()

            while queue:
                (point_x, point_y) = queue.popleft()
                reachable.add((point_x, point_y))

                for move_x, move_y in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    new_x = point_x + move_x
                    new_y = point_y + move_y

                    if (new_x, new_y) in reachable:                        
                        continue

                    # out of area
                    if new_x < 0 or new_x >= m or new_y < 0 or new_y >=n:
                        continue 

                    # check hight
                    if matrix[new_x][new_y] < matrix[point_x][point_y]:
                        continue
                    
                    # thi new point is reachable
                    queue.append((new_x, new_y))
            return reachable
        
        pacific_reachable = dfs(pacific_queue)
        atlantic_reachable = dfs(atlantic_queue)

        return list(pacific_reachable.intersection(atlantic_reachable))

# @lc code=end

