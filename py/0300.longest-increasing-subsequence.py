#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#
# https://leetcode.com/problems/longest-increasing-subsequence/description/
#
# algorithms
# Medium (45.48%)
# Likes:    10127
# Dislikes: 205
# Total Accepted:    737.6K
# Total Submissions: 1.5M
# Testcase Example:  '[10,9,2,5,3,7,101,18]'
#
# Given an integer array nums, return the length of the longest strictly
# increasing subsequence.
# 
# A subsequence is a sequence that can be derived from an array by deleting
# some or no elements without changing the order of the remaining elements. For
# example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].
# 
# 
# Example 1:
# 
# 
# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the
# length is 4.
# 
# 
# Example 2:
# 
# 
# Input: nums = [0,1,0,3,2,3]
# Output: 4
# 
# 
# Example 3:
# 
# 
# Input: nums = [7,7,7,7,7,7,7]
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 2500
# -10^4 <= nums[i] <= 10^4
# 
# 
# 
# Follow up: Can you come up with an algorithm that runs in O(n log(n)) time
# complexity?
# 
#

# @lc code=start
class Solution:
    # dp, o(n^2)
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        # dp[i] represents the length of the longest increasing subsequence that ends with the i^{th} ith element.
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)
                


# @lc code=end

