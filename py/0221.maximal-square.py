#
# @lc app=leetcode id=221 lang=python3
#
# [221] Maximal Square
#
# https://leetcode.com/problems/maximal-square/description/
#
# algorithms
# Medium (42.72%)
# Likes:    6497
# Dislikes: 139
# Total Accepted:    454.4K
# Total Submissions: 1.1M
# Testcase Example:  '[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]'
#
# Given an m x n binary matrix filled with 0's and 1's, find the largest square
# containing only 1's and return its area.
# 
# 
# Example 1:
# 
# 
# Input: matrix =
# [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# Output: 4
# 
# 
# Example 2:
# 
# 
# Input: matrix = [["0","1"],["1","0"]]
# Output: 1
# 
# 
# Example 3:
# 
# 
# Input: matrix = [["0"]]
# Output: 0
# 
# 
# 
# Constraints:
# 
# 
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 300
# matrix[i][j] is '0' or '1'.
# 
# 
#

# @lc code=start
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        if not m:
            return 0
        
        dp = [[0] * n for _ in range(m)]  # largetst square ending at i,j
        max_len = 0
        for i in range(n):
            dp[0][i] = int(matrix[0][i])
            max_len = max(max_len, dp[0][i])
        for i in range(m):
            dp[i][0] = int(matrix[i][0])
            max_len = max(max_len, dp[i][0])

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == '1':
                    # dp[i][j-1], dp[i-1][j] <= dp[i-1][j-1] + 1
                    # if all dp[i][j-1], dp[i-1][j] >= dp[i-1][j-1], they can help increase
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1
                    max_len = max(dp[i][j], max_len)
        return max_len ** 2

# @lc code=end

