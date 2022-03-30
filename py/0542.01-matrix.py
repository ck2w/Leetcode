#
# @lc app=leetcode id=542 lang=python3
#
# [542] 01 Matrix
#
# https://leetcode.com/problems/01-matrix/description/
#
# algorithms
# Medium (41.64%)
# Likes:    3885
# Dislikes: 187
# Total Accepted:    202.4K
# Total Submissions: 467.1K
# Testcase Example:  '[[0,0,0],[0,1,0],[0,0,0]]'
#
# Given an m x n binary matrix mat, return the distance of the nearest 0 for
# each cell.
# 
# The distance between two adjacent cells is 1.
# 
# 
# Example 1:
# 
# 
# Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
# Output: [[0,0,0],[0,1,0],[0,0,0]]
# 
# 
# Example 2:
# 
# 
# Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
# Output: [[0,0,0],[0,1,0],[1,2,1]]
# 
# 
# 
# Constraints:
# 
# 
# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 10^4
# 1 <= m * n <= 10^4
# mat[i][j] is either 0 or 1.
# There is at least one 0 in mat.
# 
# 
#

# @lc code=start
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        from collections import deque
        m = len(mat)
        n = len(mat[0])

        def is_border(axis):
            r, c = axis[0], axis[1]
            for move in [(0,1), (0,-1), (1,0), (-1,0)]:
                rr, cc = r + move[0], c + move[1]
                if 0 <= rr < m and 0 <= cc < n and result[rr][cc] == -1 and result[r][c] == 0:
                    return True
            return False

        result = [[0] * n for _ in range(m)]

        borders = deque()

        for i in range(m):
            for j in range(n):
                if mat[i][j] != 0:
                    result[i][j] = -1
        
        for i in range(m):
            for j in range(n):
                if is_border((i, j)):
                    borders.append((i, j))
        # print(list(borders))
        while borders:
            r, c = borders.popleft()
            for move in [(0,1), (0,-1), (1,0), (-1,0)]:
                rr, cc = r + move[0], c + move[1]
                if 0 <= rr < m and 0 <= cc < n and result[rr][cc] == -1:
                    result[rr][cc] = result[r][c] + 1
                    borders.append((rr, cc))
        
        return result

# @lc code=end

