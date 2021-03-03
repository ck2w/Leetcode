#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#
# https://leetcode.com/problems/binary-search/description/
#
# algorithms
# Easy (54.03%)
# Likes:    1175
# Dislikes: 57
# Total Accepted:    235.7K
# Total Submissions: 436.1K
# Testcase Example:  '[-1,0,3,5,9,12]\n9'
#
# Given a sorted (in ascending order) integer array nums of n elements and a
# target value, write a function to search target in nums. If target exists,
# then return its index, otherwise return -1.
# 
# 
# Example 1:
# 
# 
# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4
# 
# 
# 
# Example 2:
# 
# 
# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1
# 
# 
# 
# 
# Note:
# 
# 
# You may assume that all elements in nums are unique.
# n will be in the range [1, 10000].
# The value of each element in nums will be in the range [-9999, 9999].
# 
# 
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums)
        while lo < hi:
            mid = (hi + lo) // 2
            if nums[mid] >= target:
                hi = mid
            else:
                lo = mid + 1
        if lo == len(nums) or nums[lo] != target :
            return -1
        else:
            return lo
            
# @lc code=end

