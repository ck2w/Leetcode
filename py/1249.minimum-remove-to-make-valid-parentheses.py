#
# @lc app=leetcode id=1249 lang=python3
#
# [1249] Minimum Remove to Make Valid Parentheses
#
# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/description/
#
# algorithms
# Medium (64.16%)
# Likes:    1914
# Dislikes: 44
# Total Accepted:    177.2K
# Total Submissions: 275.9K
# Testcase Example:  '"lee(t(c)o)de)"'
#
# Given a string s of '(' , ')' and lowercase English characters. 
# 
# Your task is to remove the minimum number of parentheses ( '(' or ')', in any
# positions ) so that the resulting parentheses string is valid and return any
# valid string.
# 
# Formally, a parentheses string is valid if and only if:
# 
# 
# It is the empty string, contains only lowercase characters, or
# It can be written as AB (A concatenated with B), where A and B are valid
# strings, or
# It can be written as (A), where A is a valid string.
# 
# 
# 
# Example 1:
# 
# 
# Input: s = "lee(t(c)o)de)"
# Output: "lee(t(c)o)de"
# Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
# 
# 
# Example 2:
# 
# 
# Input: s = "a)b(c)d"
# Output: "ab(c)d"
# 
# 
# Example 3:
# 
# 
# Input: s = "))(("
# Output: ""
# Explanation: An empty string is also valid.
# 
# 
# Example 4:
# 
# 
# Input: s = "(a(b(c)d)"
# Output: "a(b(c)d)"
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 10^5
# s[i] is one of  '(' , ')' and lowercase English letters.
# 
#

# @lc code=start
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []  # save unmatch parentheses
        result = ''
        for i in range(len(s)):
            letter = s[i]
            if letter == ')' and stack and stack[-1][0] == '(':
                stack.pop()
            elif letter in '()':
                stack.append([letter, i])            

        remove_locs = set(x[1] for x in stack)
        for i in range(len(s)):
            if i not in remove_locs:
                result = result + s[i]
        return result
# @lc code=end

