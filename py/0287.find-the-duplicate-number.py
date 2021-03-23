#
# @lc app=leetcode id=287 lang=python3
#
# [287] Find the Duplicate Number
#
# https://leetcode.com/problems/find-the-duplicate-number/description/
#
# algorithms
# Medium (57.50%)
# Likes:    6897
# Dislikes: 745
# Total Accepted:    474.3K
# Total Submissions: 823.9K
# Testcase Example:  '[1,3,4,2,2]'
#
# Given an array of integers nums containing n + 1 integers where each integer
# is in the range [1, n] inclusive.
# 
# There is only one repeated number in nums, return this repeated number.
# 
# 
# Example 1:
# Input: nums = [1,3,4,2,2]
# Output: 2
# Example 2:
# Input: nums = [3,1,3,4,2]
# Output: 3
# Example 3:
# Input: nums = [1,1]
# Output: 1
# Example 4:
# Input: nums = [1,1,2]
# Output: 1
# 
# 
# Constraints:
# 
# 
# 2 <= n <= 3 * 10^4
# nums.length == n + 1
# 1 <= nums[i] <= n
# All the integers in nums appear only once except for precisely one integer
# which appears two or more times.
# 
# 
# 
# Follow up:
# 
# 
# How can we prove that at least one duplicate number must exist in nums?
# Can you solve the problem without modifying the array nums?
# Can you solve the problem using only constant, O(1) extra space?
# Can you solve the problem with runtime complexity less than O(n^2)?
# 
# 
#

# @lc code=start

# 1: sorting + binary search, time: O(nlogn), space: O(n)
# pigeon hole problem: 
# n + 1 integers where each integer is in the range [1, n] inclusive
# if sorted_nums[mid] == mid: right side, numbers before mid exist
# if sorted_nums[mid] > mid: right side, some numbers before mid do not exist, places taken by numbers after mid
# if sorted_nums[mid] < mid: left side

# class Solution:
#     def findDuplicate(self, nums: List[int]) -> int:
#         sort_nums = sorted(nums)
#         lo = 0
#         hi = len(sort_nums)
#         while lo < hi:
#             mid = (lo + hi) // 2
#             if sort_nums[mid] >= mid+1:
#                 # duplicate at right
#                 lo = mid + 1
#             elif sort_nums[mid] < mid+1:
#                 # duplicate at left
#                 hi = mid            
#         return lo

# 2: check set lenght, time: O(n), space: O(n)
# class Solution:
#     def findDuplicate(self, nums: List[int]) -> int:
#         s = set()
#         for num in nums:
#             if num in s:
#                 return num
#             else:
#                 s.add(num)

# 3: Floyd's Tortoise and Hare, time: O(n), space: O(1)
# https://blog.csdn.net/u013832707/article/details/103469112
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Find the intersection point of the two runners.
        tortoise = hare = nums[0]
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]] # hare is twice faster
            if tortoise == hare:
                break
        
        # Find the "entrance" to the cycle.
        tortoise = nums[0]
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]  # all move with tortoise speed
        
        return hare

# @lc code=end

