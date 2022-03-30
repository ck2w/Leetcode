#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (31.40%)
# Likes:    13297
# Dislikes: 689
# Total Accepted:    2M
# Total Submissions: 6.5M
# Testcase Example:  '"abcabcbb"'
#
# Given a string s, find the length of the longest substring without repeating
# characters.
# 
# 
# Example 1:
# 
# 
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# 
# 
# Example 2:
# 
# 
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# 
# 
# Example 3:
# 
# 
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a
# substring.
# 
# 
# Example 4:
# 
# 
# Input: s = ""
# Output: 0
# 
# 
# 
# Constraints:
# 
# 
# 0 <= s.length <= 5 * 10^4
# s consists of English letters, digits, symbols and spaces.
# 
# 
#

# @lc code=start
class Solution:

    # brute force
    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     def check(start, end):
    #         chars = [0] * 128
    #         for i in range(start, end + 1):
    #             c = s[i]
    #             chars[ord(c)] += 1
    #             if chars[ord(c)] > 1:
    #                 return False
    #         return True

    #     n = len(s)

    #     res = 0
    #     for i in range(n):
    #         for j in range(i, n):
    #             if check(i, j):
    #                 res = max(res, j - i + 1)
    #     return res


    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        n = len(s)
        
        i = 0
        d = {}
        max_len = 0
        
        for j in range(n):            
            if s[j] not in d:
                # new element, update j
                d[s[j]] = j
            else:
                # old element, update i by 1 step; i never back roll
                i = max(i, d[s[j]] + 1)
                d[s[j]] = j                
                
            max_len = max(max_len, j - i + 1)
        return max_len
                
# @lc code=end

