#
# @lc app=leetcode id=1163 lang=python3
#
# [1163] Last Substring in Lexicographical Order
#
# https://leetcode.com/problems/last-substring-in-lexicographical-order/description/
#
# algorithms
# Hard (34.86%)
# Likes:    216
# Dislikes: 289
# Total Accepted:    16.7K
# Total Submissions: 47.7K
# Testcase Example:  '"abab"\r'
#
# Given a string s, return the last substring of s in lexicographical
# order.
# 
# 
# 
# Example 1:
# 
# 
# Input: "abab"
# Output: "bab"
# Explanation: The substrings are ["a", "ab", "aba", "abab", "b", "ba", "bab"].
# The lexicographically maximum substring is "bab".
# 
# 
# Example 2:
# 
# 
# Input: "leetcode"
# Output: "tcode"
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= s.length <= 4 * 10^5
# s contains only lowercase English letters.
# 
# 
#

# @lc code=start
class Solution:
    def lastSubstring(self, s: str) -> str:
        '''
        首先最大字串肯定是最大后缀字串
        即如果我们当前得到了最大字符，index是它在字符串s中的下标，我们当前的答案就是 s [ index : ]
        设立左右两个指针，left记录当前遇见的最大字符，right负责往后遍历，寻找是否有更大的字符
        step负责的是：如果s[left] == s[right] 则继续比较 s [ left + i ]与 s [ right + i ] （i = 1,2,3,4,5......）的工作
        直到我们找到了其中一个更大的或者我们遇见了边界 right+step == len(s), 否则step将一直增大
        一旦找到了一个更大的，我们就把step还原回0
        '''
        s_len, left, right, step = len(s), 0, 1, 0
        while(right + step < s_len):
            if s[right + step] > s[left + step]:
                left, right, step = right , right+1, 0
            elif s[right + step] < s[left + step]:
                right, step = right+step+1, 0
            else:
                step += 1
        return s[left:]

# @lc code=end

