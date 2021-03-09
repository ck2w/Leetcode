#
# @lc app=leetcode id=394 lang=python3
#
# [394] Decode String
#
# https://leetcode.com/problems/decode-string/description/
#
# algorithms
# Medium (52.64%)
# Likes:    4678
# Dislikes: 228
# Total Accepted:    306.9K
# Total Submissions: 582K
# Testcase Example:  '"3[a]2[bc]"'
#
# Given an encoded string, return its decoded string.
# 
# The encoding rule is: k[encoded_string], where the encoded_string inside the
# square brackets is being repeated exactly k times. Note that k is guaranteed
# to be a positive integer.
# 
# You may assume that the input string is always valid; No extra white spaces,
# square brackets are well-formed, etc.
# 
# Furthermore, you may assume that the original data does not contain any
# digits and that digits are only for those repeat numbers, k. For example,
# there won't be input like 3a or 2[4].
# 
# 
# Example 1:
# Input: s = "3[a]2[bc]"
# Output: "aaabcbc"
# Example 2:
# Input: s = "3[a2[c]]"
# Output: "accaccacc"
# Example 3:
# Input: s = "2[abc]3[cd]ef"
# Output: "abcabccdcdcdef"
# Example 4:
# Input: s = "abc3[cd]xyz"
# Output: "abccdcdcdxyz"
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 30
# s consists of lowercase English letters, digits, and square brackets
# '[]'.
# s is guaranteed to be a valid input.
# All the integers in s are in the range [1, 300].
# 
# 
#

# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:
        alphas = ''
        digits = ''
        stack = []
        for letter in s:
            if letter.isalpha():
                alphas = alphas + letter
            elif letter.isdigit():
                digits = digits + letter
            elif letter == '[':
                stack.append((alphas, digits))
                alphas = ''
                digits = ''
            elif letter == ']':
                prev_alphas, prev_digits = stack.pop()
                alphas = prev_alphas + int(prev_digits) * alphas
        return alphas
# @lc code=end

