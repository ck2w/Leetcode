#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
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

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            if not nums[i] in d:                
                d[nums[i]] = i
            if target - nums[i] in d and d[target - nums[i]] < i:                    
                return [d[target - nums[i]], i]

