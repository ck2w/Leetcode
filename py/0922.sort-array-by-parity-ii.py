#
# @lc app=leetcode id=922 lang=python3
#
# [922] Sort Array By Parity II
#
# https://leetcode.com/problems/sort-array-by-parity-ii/description/
#
# algorithms
# Easy (70.55%)
# Likes:    1619
# Dislikes: 69
# Total Accepted:    175.2K
# Total Submissions: 248.2K
# Testcase Example:  '[4,2,5,7]'
#
# Given an array of integers nums, half of the integers in nums are odd, and
# the other half are even.
# 
# Sort the array so that whenever nums[i] is odd, i is odd, and whenever
# nums[i] is even, i is even.
# 
# Return any answer array that satisfies this condition.
# 
# 
# Example 1:
# 
# 
# Input: nums = [4,2,5,7]
# Output: [4,5,2,7]
# Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.
# 
# 
# Example 2:
# 
# 
# Input: nums = [2,3]
# Output: [2,3]
# 
# 
# 
# Constraints:
# 
# 
# 2 <= nums.length <= 2 * 10^4
# nums.length is even.
# Half of the integers in nums are even.
# 0 <= nums[i] <= 1000
# 
# 
# 
# Follow Up: Could you solve it in-place?
# 
#

# @lc code=start
from cmath import e


class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        odd_num = [x for x in nums if x % 2 == 1]
        even_num = [x for x in nums if x % 2 == 0]
        result = [0] * len(nums)
        result[::2] = even_num
        result[1::2] = odd_num
        return result
        
# @lc code=end

