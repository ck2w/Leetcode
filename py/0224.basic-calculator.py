#
# @lc app=leetcode id=224 lang=python3
#
# [224] Basic Calculator
#
# https://leetcode.com/problems/basic-calculator/description/
#
# algorithms
# Hard (38.13%)
# Likes:    2052
# Dislikes: 163
# Total Accepted:    199K
# Total Submissions: 521.1K
# Testcase Example:  '"1 + 1"'
#
# Given a string s representing an expression, implement a basic calculator to
# evaluate it.
# 
# 
# Example 1:
# 
# 
# Input: s = "1 + 1"
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: s = " 2-1 + 2 "
# Output: 3
# 
# 
# Example 3:
# 
# 
# Input: s = "(1+(4+5+2)-3)+(6+8)"
# Output: 23
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 3 * 10^5
# s consists of digits, '+', '-', '(', ')', and ' '.
# s represents a valid expression.
# 
# 
#

# @lc code=start
class Solution:
    def calculate(self, s: str) -> int:

        def evaludate_plain(ss):
            result = 0
            num = ''
            symbol = '+'
            for i in ss:
                if i.isdigit():
                    num = num + i
                elif i in ['+', '-']:
                    if num:                  
                        result = result + int(symbol + num)                    
                    symbol = i
                    num = ''
            if symbol == '+':
                result = result + int(num)
            elif symbol == '-':
                result = result - int(num)
            return result
                  

        digits = ''
        stack = []
        for letter in s:
            if letter.isdigit() or letter in ['+', '-']:
                digits = digits + letter            
            elif letter == '(':
                stack.append(digits)
                digits = ''                
            elif letter == ')':
                prev_digits = stack.pop()
                new_result = evaludate_plain(digits)

                # continuous minus (2--1)
                if new_result < 0:
                    if not prev_digits or prev_digits[-1] == '+':
                        prev_digits = prev_digits[:-1]
                    elif prev_digits[-1] == '-':
                        prev_digits = prev_digits[:-1] + '+'
                        new_result = -new_result
                digits = prev_digits + str(new_result)
        return evaludate_plain(digits)

# @lc code=end

