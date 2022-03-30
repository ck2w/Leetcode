#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#
# https://leetcode.com/problems/first-unique-character-in-a-string/description/
#
# algorithms
# Easy (54.59%)
# Likes:    4285
# Dislikes: 177
# Total Accepted:    939K
# Total Submissions: 1.7M
# Testcase Example:  '"leetcode"'
#
# Given a string s, find the first non-repeating character in it and return its
# index. If it does not exist, return -1.
# 
# 
# Example 1:
# Input: s = "leetcode"
# Output: 0
# Example 2:
# Input: s = "loveleetcode"
# Output: 2
# Example 3:
# Input: s = "aabb"
# Output: -1
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 10^5
# s consists of only lowercase English letters.
# 
# 
#

# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for i in range(len(s)):
            if s[i] in d:
                d[s[i]].append(i)
            else:
                d[s[i]] = [i]
                
        min_index = len(s)
        for k, v in d.items():
            if len(v) == 1:
                min_index = min(min_index, v[0])
                
        if min_index == len(s):
            min_index = -1
        return min_index
            
# @lc code=end

