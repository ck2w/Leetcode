#
# @lc app=leetcode id=905 lang=python3
#
# [905] Sort Array By Parity
#
# https://leetcode.com/problems/sort-array-by-parity/description/
#
# algorithms
# Easy (74.80%)
# Likes:    2446
# Dislikes: 109
# Total Accepted:    412.7K
# Total Submissions: 551.8K
# Testcase Example:  '[3,1,2,4]'
#
# Given an integer array nums, move all the even integers at the beginning of
# the array followed by all the odd integers.
# 
# Return any array that satisfies this condition.
# 
# 
# Example 1:
# 
# 
# Input: nums = [3,1,2,4]
# Output: [2,4,3,1]
# Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be
# accepted.
# 
# 
# Example 2:
# 
# 
# Input: nums = [0]
# Output: [0]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 5000
# 0 <= nums[i] <= 5000
# 
# 
#

# @lc code=start
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        return ([x for x in A if x % 2 == 0] +
                [x for x in A if x % 2 == 1])
        
# @lc code=end

