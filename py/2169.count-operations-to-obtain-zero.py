
# @lc app=leetcode id=2169 lang=python3
#
# [2169] Count Operations to Obtain Zero
#
# @lc code=start
class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        count = 0
        while num1 and num2:
            count += 1
            if num1 > num2:
                num1 = num1 - num2
            elif num1 < num2:
                num2 = num2 - num1
            else:
                return count
        return count
# @lc code=end
