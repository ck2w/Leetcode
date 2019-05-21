#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#
# https://leetcode.com/problems/sqrtx/description/
#
# algorithms
# Easy (30.65%)
# Total Accepted:    333.5K
# Total Submissions: 1.1M
# Testcase Example:  '4'
#
# Implement int sqrt(int x).
# 
# Compute and return the square root of x, where x is guaranteed to be a
# non-negative integer.
# 
# Since the return type is an integer, the decimal digits are truncated and
# only the integer part of the result is returned.
# 
# Example 1:
# 
# 
# Input: 4
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since 
# the decimal part is truncated, 2 is returned.
# 
# 
#
# 1 direct solve (56ms)
# class Solution:
#     def mySqrt(self, x: int) -> int:
#         return int(x ** 0.5)

# 2 newton's method (80ms)
class Solution:
    def mySqrt(self, x: int) -> int:
        guess = x/2
        while guess**2-x > 0.1 or guess**2-x < -0.1:
            guess = guess - (guess**2-x)/(2*guess**1)
            print(guess)
        return int(guess)


