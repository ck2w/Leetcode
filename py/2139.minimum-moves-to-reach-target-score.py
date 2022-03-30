
# @lc app=leetcode id=2139 lang=python3
#
# [2139] Minimum Moves to Reach Target Score
#
# https://leetcode.com/problems/minimum-moves-to-reach-target-score/
# @lc code=start
class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        steps = 0        
        
        while maxDoubles > 0 and target > 1:
            if target % 2 == 0:
                target /= 2
                steps = steps + 1
                maxDoubles -= 1
            else:
                target -= 1
                steps = steps + 1
            
        steps = steps + target - 1
        
        return int(steps)

# @lc code=end
