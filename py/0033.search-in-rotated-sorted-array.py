#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#
# https://leetcode.com/problems/search-in-rotated-sorted-array/description/
#
# algorithms
# Medium (37.30%)
# Likes:    12009
# Dislikes: 812
# Total Accepted:    1.3M
# Total Submissions: 3.5M
# Testcase Example:  '[4,5,6,7,0,1,2]\n0'
#
# There is an integer array nums sorted in ascending order (with distinct
# values).
# 
# Prior to being passed to your function, nums is possibly rotated at an
# unknown pivot index k (1 <= k < nums.length) such that the resulting array is
# [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]
# (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3
# and become [4,5,6,7,0,1,2].
# 
# Given the array nums after the possible rotation and an integer target,
# return the index of target if it is in nums, or -1 if it is not in nums.
# 
# You must write an algorithm with O(log n) runtime complexity.
# 
# 
# Example 1:
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
# Example 3:
# Input: nums = [1], target = 0
# Output: -1
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 5000
# -10^4 <= nums[i] <= 10^4
# All values of nums are unique.
# nums is an ascending array that is possibly rotated.
# -10^4 <= target <= 10^4
# 
# 
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start_index = -1
        n = len(nums)
        
        if not nums:
            return -1
        
        if len(nums) == 1 :
            if nums[0] != target:
                return -1
            else:
                return 0    
            
        if len(nums) == 2:
            if nums[0] == target:
                return 0
            elif nums[1] == target:
                return 1
            else:
                return -1
        
        # start index        
        s0 = nums[0]
        s1 = nums[-1]
        if s0 < s1:
            start_index = 0
        else:
            # binary search to get start index
            lo, hi = 0, len(nums) - 1            
            while lo <= hi:
                mid = (lo + hi) // 2                                                        
                
                if nums[mid] < nums[(mid+1)%n] < nums[(mid-1)%n]:
                    # smallest
                    start_index = mid
                    break
                elif nums[(mid+1)%n] < nums[(mid-1)%n] < nums[mid]:
                    # largest
                    start_index = (mid+1)%n
                    break
                elif nums[mid] < s1:
                    hi = mid - 1
                elif nums[mid] > s0:
                    lo = mid + 1
                else:                                        
                    print('not happen')
        
        # search value
        lo = start_index
        hi = start_index + n - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid%n] == target:
                return mid % n
            elif nums[mid%n] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return -1           
  
# @lc code=end

