#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#
# https://leetcode.com/problems/daily-temperatures/description/
#
# algorithms
# Medium (64.56%)
# Likes:    3923
# Dislikes: 120
# Total Accepted:    223.3K
# Total Submissions: 345.4K
# Testcase Example:  '[73,74,75,71,69,72,76,73]'
#
# 
# Given a list of daily temperatures T, return a list such that, for each day
# in the input, tells you how many days you would have to wait until a warmer
# temperature.  If there is no future day for which this is possible, put 0
# instead.
# 
# For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76,
# 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].
# 
# 
# Note:
# The length of temperatures will be in the range [1, 30000].
# Each temperature will be an integer in the range [30, 100].
# 
#

# @lc code=start
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []
        result = [0] * len(T)
        for loc, val in enumerate(T):            
            while stack:
                if val > stack[-1][1]:
                    prev_val =  stack.pop()                   
                    result[prev_val[0]] = loc - prev_val[0]                    
                else:
                    break
            stack.append((loc, val))
        
        return result

# @lc code=end

