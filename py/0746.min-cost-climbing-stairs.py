#
# @lc app=leetcode id=746 lang=python3
#
# [746] Min Cost Climbing Stairs
#
# https://leetcode.com/problems/min-cost-climbing-stairs/description/
#
# algorithms
# Easy (57.29%)
# Likes:    5100
# Dislikes: 927
# Total Accepted:    387.7K
# Total Submissions: 676.5K
# Testcase Example:  '[10,15,20]'
#
# You are given an integer array cost where cost[i] is the cost of i^th step on
# a staircase. Once you pay the cost, you can either climb one or two steps.
# 
# You can either start from the step with index 0, or the step with index 1.
# 
# Return the minimum cost to reach the top of the floor.
# 
# 
# Example 1:
# 
# 
# Input: cost = [10,15,20]
# Output: 15
# Explanation: You will start at index 1.
# - Pay 15 and climb two steps to reach the top.
# The total cost is 15.
# 
# 
# Example 2:
# 
# 
# Input: cost = [1,100,1,1,1,100,1,1,100,1]
# Output: 6
# Explanation: You will start at index 0.
# - Pay 1 and climb two steps to reach index 2.
# - Pay 1 and climb two steps to reach index 4.
# - Pay 1 and climb two steps to reach index 6.
# - Pay 1 and climb one step to reach index 7.
# - Pay 1 and climb two steps to reach index 9.
# - Pay 1 and climb one step to reach the top.
# The total cost is 6.
# 
# 
# 
# Constraints:
# 
# 
# 2 <= cost.length <= 1000
# 0 <= cost[i] <= 999
# 
# 
#

# @lc code=start
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * n
        for i in range(n-1, -1, -1):
            if i >= n - 2:
                dp[i] = cost[i]
            else:
                dp[i] = cost[i] + min(dp[i+1], dp[i+2])
        return min(dp[0], dp[1])

# @lc code=end

