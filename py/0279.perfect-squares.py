#
# @lc app=leetcode id=279 lang=python3
#
# [279] Perfect Squares
#
# https://leetcode.com/problems/perfect-squares/description/
#
# algorithms
# Medium (49.80%)
# Likes:    6053
# Dislikes: 274
# Total Accepted:    488.8K
# Total Submissions: 950.8K
# Testcase Example:  '12'
#
# Given an integer n, return the least number of perfect square numbers that
# sum to n.
# 
# A perfect square is an integer that is the square of an integer; in other
# words, it is the product of some integer with itself. For example, 1, 4, 9,
# and 16 are perfect squares while 3 and 11 are not.
# 
# 
# Example 1:
# 
# 
# Input: n = 12
# Output: 3
# Explanation: 12 = 4 + 4 + 4.
# 
# 
# Example 2:
# 
# 
# Input: n = 13
# Output: 2
# Explanation: 13 = 4 + 9.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 10^4
# 
# 
#

# @lc code=start
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n+1)
        square_nums = [i**2 for i in range(1, int(n**0.5)+1)]
        for i in range(0, int(n**0.5) + 1):
            dp[i**2] = 1
        dp[0] = 0
        for i in range(1, n+1):
            for square_num in square_nums:
                if i < square_num:
                    break
                dp[i] = min(dp[i], dp[i-square_num]+1) 
        return dp[n]

# @lc code=end

