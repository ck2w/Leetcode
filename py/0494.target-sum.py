#
# @lc app=leetcode id=494 lang=python3
#
# [494] Target Sum
#
# https://leetcode.com/problems/target-sum/description/
#
# algorithms
# Medium (45.52%)
# Likes:    5865
# Dislikes: 229
# Total Accepted:    307.5K
# Total Submissions: 678.4K
# Testcase Example:  '[1,1,1,1,1]\n3'
#
# You are given an integer array nums and an integer target.
# 
# You want to build an expression out of nums by adding one of the symbols '+'
# and '-' before each integer in nums and then concatenate all the
# integers.
# 
# 
# For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1
# and concatenate them to build the expression "+2-1".
# 
# 
# Return the number of different expressions that you can build, which
# evaluates to target.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,1,1,1,1], target = 3
# Output: 5
# Explanation: There are 5 ways to assign symbols to make the sum of nums be
# target 3.
# -1 + 1 + 1 + 1 + 1 = 3
# +1 - 1 + 1 + 1 + 1 = 3
# +1 + 1 - 1 + 1 + 1 = 3
# +1 + 1 + 1 - 1 + 1 = 3
# +1 + 1 + 1 + 1 - 1 = 3
# 
# 
# Example 2:
# 
# 
# Input: nums = [1], target = 1
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 20
# 0 <= nums[i] <= 1000
# 0 <= sum(nums[i]) <= 1000
# -1000 <= target <= 1000
# 
# 
#

# @lc code=start
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        visited = {}

        def helper(i, target):
            if (i, target) in visited:
                return visited[(i, target)]
            if i == 1:
                if nums[0] == target or nums[0] == -target:
                    if target == 0:
                        result = 2
                    else:
                        result = 1
                else:
                    result = 0
            else:
                result = helper(i-1, target - nums[i-1]) + helper(i-1, target + nums[i-1])
            visited[(i, target)] = result
            # print(nums, target, result)
            return result
        return helper(len(nums), target)
# @lc code=end

