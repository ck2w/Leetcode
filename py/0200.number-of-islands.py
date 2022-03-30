#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#
# https://leetcode.com/problems/number-of-islands/description/
#
# algorithms
# Medium (50.53%)
# Likes:    11488
# Dislikes: 291
# Total Accepted:    1.3M
# Total Submissions: 2.6M
# Testcase Example:  '[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]'
#
# Given an m x n 2D binary grid grid which represents a map of '1's (land) and
# '0's (water), return the number of islands.
# 
# An island is surrounded by water and is formed by connecting adjacent lands
# horizontally or vertically. You may assume all four edges of the grid are all
# surrounded by water.
# 
# 
# Example 1:
# 
# 
# Input: grid = [
# ⁠ ["1","1","1","1","0"],
# ⁠ ["1","1","0","1","0"],
# ⁠ ["1","1","0","0","0"],
# ⁠ ["0","0","0","0","0"]
# ]
# Output: 1
# 
# 
# Example 2:
# 
# 
# Input: grid = [
# ⁠ ["1","1","0","0","0"],
# ⁠ ["1","1","0","0","0"],
# ⁠ ["0","0","1","0","0"],
# ⁠ ["0","0","0","1","1"]
# ]
# Output: 3
# 
# 
# 
# Constraints:
# 
# 
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] is '0' or '1'.
# 
# 
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        from collections import deque
        q = deque()
        visited = set()
        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        m = len(grid)
        n = len(grid[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if (i, j) in visited or grid[i][j] == '0':
                    continue
                count += 1
                visited.add((i, j))
                q.append((i, j))
                while q:
                    point = q.popleft()
                    print(point)
                    r = point[0]
                    c = point[1]
                    for move in moves:
                        new_r = r + move[0]
                        new_c = c + move[1]
                        if (new_r, new_c) in visited:
                            continue
                        if new_r < 0 or new_r >= m or new_c < 0 or new_c >= n or grid[new_r][new_c] == '0':
                            continue
                        new_point = (new_r, new_c)
                        visited.add(new_point)
                        q.append(new_point)
        return count

# @lc code=end

