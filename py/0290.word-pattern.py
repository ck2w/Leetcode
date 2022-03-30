#
# @lc app=leetcode id=290 lang=python3
#
# [290] Word Pattern
#
# https://leetcode.com/problems/word-pattern/description/
#
# algorithms
# Easy (38.65%)
# Likes:    3040
# Dislikes: 345
# Total Accepted:    324.8K
# Total Submissions: 815.2K
# Testcase Example:  '"abba"\n"dog cat cat dog"'
#
# Given a pattern and a string s, find if s follows the same pattern.
# 
# Here follow means a full match, such that there is a bijection between a
# letter in pattern and a non-empty word in s.
# 
# 
# Example 1:
# 
# 
# Input: pattern = "abba", s = "dog cat cat dog"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: pattern = "abba", s = "dog cat cat fish"
# Output: false
# 
# 
# Example 3:
# 
# 
# Input: pattern = "aaaa", s = "dog cat cat dog"
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# 1 <= pattern.length <= 300
# pattern contains only lower-case English letters.
# 1 <= s.length <= 3000
# s contains only lowercase English letters and spaces ' '.
# s does not contain any leading or trailing spaces.
# All the words in s are separated by a single space.
# 
# 
#

# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        lst = s.split(' ')
        if len(lst) != len(pattern):
            return False
        d1 = {}
        d2 = {}
        for i in range(len(pattern)):
            p = pattern[i]
            v = lst[i]
            if p in d1:
                if d1[p] != v:
                    return False
            else:
                d1[p] = v
            if v in d2:
                if d2[v] != p:
                    return False
            else:
                d2[v] = p
        return True

        

# @lc code=end

