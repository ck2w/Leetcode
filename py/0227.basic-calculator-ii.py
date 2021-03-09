#
# @lc app=leetcode id=227 lang=python3
#
# [227] Basic Calculator II
#
# https://leetcode.com/problems/basic-calculator-ii/description/
#
# algorithms
# Medium (38.53%)
# Likes:    2193
# Dislikes: 344
# Total Accepted:    254.2K
# Total Submissions: 658.7K
# Testcase Example:  '"3+2*2"'
#
# Given a string s which represents an expression, evaluate this expression and
# return its value. 
# 
# The integer division should truncate toward zero.
# 
# 
# Example 1:
# Input: s = "3+2*2"
# Output: 7
# Example 2:
# Input: s = " 3/2 "
# Output: 1
# Example 3:
# Input: s = " 3+5 / 2 "
# Output: 5
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 3 * 10^5
# s consists of integers and operators ('+', '-', '*', '/') separated by some
# number of spaces.
# s represents a valid expression.
# All the integers in the expression are non-negative integers in the range [0,
# 2^31 - 1].
# The answer is guaranteed to fit in a 32-bit integer.
# 
# 
#

# @lc code=start
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = ''
        symbol = '+'
        for i in s:
            if i == ' ':
                continue
            if i.isdigit():
                num = num + i
            else:
                if symbol == '+':
                    stack.append(int(num))
                elif symbol == '-':
                    stack.append(-int(num))
                elif symbol == '*':
                    stack.append(int(stack.pop() * int(num)))
                elif symbol == '/':
                    stack.append(int(stack.pop() / int(num)))
                if i in ['+', '-', '*' ,'/']:
                    symbol = i
                    num = ''
        if symbol == '+':
            stack.append(int(num))
        elif symbol == '-':
            stack.append(-int(num))
        elif symbol == '*':
            stack.append(int(stack.pop() * int(num)))
        elif symbol == '/':
            stack.append(int(stack.pop() / int(num)))

        # sum up
        result = 0
        while stack:
            result = result + stack.pop()
        return int(result)
           

# @lc code=end

