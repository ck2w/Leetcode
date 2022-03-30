
# @lc app=leetcode id=2148 lang=python3
#
# [2148] Count Elements With Strictly Smaller and Greater Elements
#
# @lc code=start

class Solution:
    def countElements(self, nums: List[int]) -> int:        
        min_val = min(nums)
        max_val = max(nums)
        count = 0
        for i in nums:
            if min_val < i < max_val:
                count += 1
        return count

# @lc code=end
