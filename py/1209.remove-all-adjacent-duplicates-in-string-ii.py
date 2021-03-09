#
# @lc app=leetcode id=1209 lang=python3
#
# [1209] Remove All Adjacent Duplicates in String II
#
# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/description/
#
# algorithms
# Medium (57.56%)
# Likes:    1125
# Dislikes: 26
# Total Accepted:    68.2K
# Total Submissions: 118.4K
# Testcase Example:  '"abcd"\n2'
#
# Given a string s, a k duplicate removal consists of choosing k adjacent and
# equal letters from s and removing them causing the left and the right side of
# the deleted substring to concatenate together.
# 
# We repeatedly make k duplicate removals on s until we no longer can.
# 
# Return the final string after all such duplicate removals have been made.
# 
# It is guaranteed that the answer is unique.
# 
# 
# Example 1:
# 
# 
# Input: s = "abcd", k = 2
# Output: "abcd"
# Explanation: There's nothing to delete.
# 
# Example 2:
# 
# 
# Input: s = "deeedbbcccbdaa", k = 3
# Output: "aa"
# Explanation: 
# First delete "eee" and "ccc", get "ddbbbdaa"
# Then delete "bbb", get "dddaa"
# Finally delete "ddd", get "aa"
# 
# Example 3:
# 
# 
# Input: s = "pbbcggttciiippooaais", k = 2
# Output: "ps"
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 10^5
# 2 <= k <= 10^4
# s only contains lower case English letters.
# 
# 
#

# @lc code=start
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for i in s:
            if not stack:
                stack.append([1, i])
            else:
                if stack[-1][1] == i:
                    stack[-1][0] += 1
                    if stack[-1][0] >= k:
                        stack[-1][0] -= k                    
                    if stack[-1][0] == 0:
                        stack.pop()
                else:
                    stack.append([1, i])
        result = ''
        while stack:
            pop_val = stack.pop()
            result = result + pop_val[0] * pop_val[1]
        
        return result[::-1]


# @lc code=end

