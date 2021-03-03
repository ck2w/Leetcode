#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#
# https://leetcode.com/problems/powx-n/description/
#
# algorithms
# Medium (30.92%)
# Likes:    2161
# Dislikes: 3621
# Total Accepted:    600.4K
# Total Submissions: 1.9M
# Testcase Example:  '2.00000\n10'
#
# Implement pow(x, n), which calculates x raised to the power n (i.e. x^n).
# 
# 
# Example 1:
# 
# 
# Input: x = 2.00000, n = 10
# Output: 1024.00000
# 
# 
# Example 2:
# 
# 
# Input: x = 2.10000, n = 3
# Output: 9.26100
# 
# 
# Example 3:
# 
# 
# Input: x = 2.00000, n = -2
# Output: 0.25000
# Explanation: 2^-2 = 1/2^2 = 1/4 = 0.25
# 
# 
# 
# Constraints:
# 
# 
# -100.0 < x < 100.0
# -2^31 <= n <= 2^31-1
# -10^4 <= x^n <= 10^4
# 
# 
#

# @lc code=start

# 1: easy way
# class Solution:
#     def myPow(self, x: float, n: int) -> float:
#         return x ** n

# 2: recursive
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def recurse(n):
            ans = 1
            if(n == 0):
                return 1
            if(n==1):
                return x
            if(n == 2):
                return x * x
            
            if(n%2 == 0):
                ans = recurse(n//2)
                return ans * ans
            if( n%2 == 1):
                ans = recurse(n//2) * recurse((n//2) + 1)
                return ans
            
        if( n < 0 ):
            x = 1/x
            n = -n
        return recurse(n)
# @lc code=end

