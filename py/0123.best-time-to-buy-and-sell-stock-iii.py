#
# @lc app=leetcode id=123 lang=python3
#
# [123] Best Time to Buy and Sell Stock III
#
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/description/
#
# algorithms
# Hard (32.90%)
# Total Accepted:    139.8K
# Total Submissions: 423.4K
# Testcase Example:  '[3,3,5,0,0,3,1,4]'
#
# Say you have an array for which the i^th element is the price of a given
# stock on day i.
# 
# Design an algorithm to find the maximum profit. You may complete at most two
# transactions.
# 
# Note: You may not engage in multiple transactions at the same time (i.e., you
# must sell the stock before you buy again).
# 
# Example 1:
# 
# 
# Input: [3,3,5,0,0,3,1,4]
# Output: 6
# Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit =
# 3-0 = 3.
# Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 =
# 3.
# 
# Example 2:
# 
# 
# Input: [1,2,3,4,5]
# Output: 4
# Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit =
# 5-1 = 4.
# Note that you cannot buy on day 1, buy on day 2 and sell them later, as you
# are
# engaging multiple transactions at the same time. You must sell before buying
# again.
# 
# 
# Example 3:
# 
# 
# Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.
# 
# 1 brutal force (Time Limit Exceeded)
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         profit = 0
#         for s1 in range(len(prices)):
#             for e1 in range(s1+1, len(prices)):
#                 p1 = prices[e1] - prices[s1]
#                 p2 = 0
#                 for s2 in range(e1, len(prices)):
#                     for e2 in range(s2+1, len(prices)):
#                         p2 = max(p2, max(0, prices[e2] - prices[s2]))
#                 profit = max(profit, p1 + p2)
#         return profit

# 2 dynamic programming (64ms)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0: return 0
        minvalue = prices[0]
        pre_profit = [0] * len(prices)
        post_profit = [0] * len(prices)
        for i in range(1,len(prices)):
            minvalue = min(minvalue, prices[i])
            pre_profit[i] = max(pre_profit[i-1], prices[i] - minvalue)
        
        maxvalue = prices[-1]
        for i in range(len(prices)-2,-1,-1):
            maxvalue = max(maxvalue, prices[i])
            post_profit[i] = max(post_profit[1], maxvalue-prices[i])
        
        maxprofit = 0
        for i in range(len(prices)):
            maxprofit = max(maxprofit, pre_profit[i]+post_profit[i])        
        return maxprofit


