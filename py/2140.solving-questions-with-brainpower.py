
# @lc app=leetcode id=2140 lang=python3
#
# [2140] Solving Questions With Brainpower 
#
# https://leetcode.com/problems/solving-questions-with-brainpower/
# @lc code=start
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        if not questions:
            return 0        
        n = len(questions)
        if n == 1:
            return questions[0][0]
        
        dp = [0] * n  # profit if have option to choose
        dp[n-1] = questions[n-1][0]
        i = n - 2
        while i >= 0:
            curr_profit = questions[i][0]
            next_steps = questions[i][1]
            if i + next_steps+1 < n:
                next_profit = dp[i+next_steps+1]
            else:
                next_profit = 0
            take_profit = curr_profit + next_profit
            skip_profit = dp[i+1]
            dp[i] = max(take_profit, skip_profit)
            # print(curr_profit, next_steps, next_profit, take_profit, skip_profit, dp[i])
            i -= 1
            
        return dp[0]

# @lc code=end
