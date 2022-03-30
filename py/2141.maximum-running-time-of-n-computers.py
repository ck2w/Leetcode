
# @lc app=leetcode id=2141 lang=python3
#
# [2141] Maximum Running Time of N Computers
#
# https://leetcode.com/problems/maximum-running-time-of-n-computers/
# @lc code=start


# upper bound: is to use all baterial evenly, sum(A) / n minutes.


class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        batteries = sorted(batteries, reverse=True)
        su = sum(batteries)
        for t in batteries:
            if t > su // n:
                n -= 1
                su -= t
            else:
                return su // n

# @lc code=end
