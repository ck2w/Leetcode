#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
# https://leetcode.com/problems/two-sum/description/
#
# algorithms
# Easy (41.89%)
# Total Accepted:    1.5M
# Total Submissions: 3.6M
# Testcase Example:  '[2,7,11,15]\n9'
#
# Given an array of integers, return indices of the two numbers such that they
# add up to a specific target.
# 
# You may assume that each input would have exactly one solution, and you may
# not use the same element twice.
# 
# Example:
# 
# 
# Given nums = [2, 7, 11, 15], target = 9,
# 
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
# 
# 
# 
# 
#
# 1 brute force (5248ms)
# loop possible combinations
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]   
#
#
# 2 hashtable (60ms)
# avoid repeated combination (dictionary in python)
# ref:
# https://zhuanlan.zhihu.com/p/28947993

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            if not nums[i] in d:                
                d[nums[i]] = i
            if target - nums[i] in d and d[target - nums[i]] < i:                    
                return [d[target - nums[i]], i]

