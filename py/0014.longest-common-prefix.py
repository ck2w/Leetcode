#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#
# https://leetcode.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (36.13%)
# Likes:    3848
# Dislikes: 2165
# Total Accepted:    973K
# Total Submissions: 2.7M
# Testcase Example:  '["flower","flow","flight"]'
#
# Write a function to find the longest common prefix string amongst an array of
# strings.
# 
# If there is no common prefix, return an empty string "".
# 
# 
# Example 1:
# 
# 
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# 
# 
# Example 2:
# 
# 
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# 
# 
# 
# Constraints:
# 
# 
# 0 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lower-case English letters.
# 
# 
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''

        for i in range(len(strs[0])):
            curr_letter = strs[0][i]

            for s in strs:
                if i >= len(s):
                    return strs[0][:i]
                elif s[i] != curr_letter:
                    return strs[0][:i]
        return strs[0]



# @lc code=end

