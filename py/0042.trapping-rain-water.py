#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#
# https://leetcode.com/problems/trapping-rain-water/description/
#
# algorithms
# Hard (51.14%)
# Likes:    10240
# Dislikes: 157
# Total Accepted:    690.6K
# Total Submissions: 1.3M
# Testcase Example:  '[0,1,0,2,1,0,1,3,2,1,2,1]'
#
# Given n non-negative integers representing an elevation map where the width
# of each bar is 1, compute how much water it can trap after raining.
# 
# 
# Example 1:
# 
# 
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array
# [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section)
# are being trapped.
# 
# 
# Example 2:
# 
# 
# Input: height = [4,2,0,3,2,5]
# Output: 9
# 
# 
# 
# Constraints:
# 
# 
# n == height.length
# 0 <= n <= 3 * 10^4
# 0 <= height[i] <= 10^5
# 
# 
#
# 1: dp
# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        result = []
        left_max = [height[0]]
        right_max = [height[-1]]
        for i in height[1:]:
            left_max.append(max(left_max[-1], i))
        for i in height[-2::-1]:
            right_max.append(max(right_max[-1], i))
        right_max = right_max[::-1] 
        
        for loc in range(len(height)):
            val = min(left_max[loc], right_max[loc]) - height[loc]
            result.append(val)
        return sum(result)
        

# @lc code=end

