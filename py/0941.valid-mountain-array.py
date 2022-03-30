#
# @lc app=leetcode id=941 lang=python3
#
# [941] Valid Mountain Array
#
# https://leetcode.com/problems/valid-mountain-array/description/
#
# algorithms
# Easy (32.33%)
# Likes:    1475
# Dislikes: 123
# Total Accepted:    232.7K
# Total Submissions: 711K
# Testcase Example:  '[2,1]'
#
# Given an array of integers arr, return true if and only if it is a valid
# mountain array.
# 
# Recall that arr is a mountain array if and only if:
# 
# 
# arr.length >= 3
# There exists some i with 0 < i < arr.length - 1 such that:
# 
# arr[0] < arr[1] < ... < arr[i - 1] < arr[i] 
# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
# 
# 
# 
# 
# 
# Example 1:
# Input: arr = [2,1]
# Output: false
# Example 2:
# Input: arr = [3,5,5]
# Output: false
# Example 3:
# Input: arr = [0,3,2,1]
# Output: true
# 
# 
# Constraints:
# 
# 
# 1 <= arr.length <= 10^4
# 0 <= arr[i] <= 10^4
# 
# 
#

# @lc code=start
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        prev = -1
        asc = True
        asc_count = 0
        desc_count = 0
        for num in arr:
            if asc:
                if num > prev:
                    prev = num
                    asc_count += 1
                    continue
                elif num < prev:
                    asc = False
                    desc_count += 1
                    prev = num
                else:
                    return False
            else:
                if num < prev:
                    prev = num
                    desc_count += 1
                    continue
                else:
                    return False
        if asc_count-1 and desc_count:
            return True
        else:
            return False
# @lc code=end

