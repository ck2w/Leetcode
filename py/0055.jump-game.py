#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#
# https://leetcode.com/problems/jump-game/description/
#
# algorithms
# Medium (35.14%)
# Likes:    5773
# Dislikes: 402
# Total Accepted:    589.1K
# Total Submissions: 1.7M
# Testcase Example:  '[2,3,1,1,4]'
#
# Given an array of non-negative integers nums, you are initially positioned at
# the first index of the array.
# 
# Each element in the array represents your maximum jump length at that
# position.
# 
# Determine if you are able to reach the last index.
# 
# 
# Example 1:
# 
# 
# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
# 
# 
# Example 2:
# 
# 
# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum
# jump length is 0, which makes it impossible to reach the last index.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 3 * 10^4
# 0 <= nums[i] <= 10^5
# 
# 
#

# @lc code=start

# 1. recursively solve, Time Limit Exceeded
# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#         if len(nums) <= 1:
#             return True

#         cond = []
#         if nums[0] == 0:
#             return False
#         for i in range(1, nums[0]+1):
#             if i < len(nums):
#                 cond.append(self.canJump(nums[i:]))
#         return reduce(lambda x, y: x or y, cond)


# 2.greedy
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        lastjump = len(nums) - 1
        for i in range(len(nums)-2, -1, -1):
            print(i)
            if i + nums[i] >= lastjump:
                lastjump = i
        return lastjump == 0

# @lc code=end

