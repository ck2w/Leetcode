#
# @lc app=leetcode id=605 lang=python3
#
# [605] Can Place Flowers
#
# https://leetcode.com/problems/can-place-flowers/description/
#
# algorithms
# Easy (31.55%)
# Likes:    2237
# Dislikes: 573
# Total Accepted:    239K
# Total Submissions: 736.5K
# Testcase Example:  '[1,0,0,0,1]\n1'
#
# You have a long flowerbed in which some of the plots are planted, and some
# are not. However, flowers cannot be planted in adjacent plots.
# 
# Given an integer array flowerbed containing 0's and 1's, where 0 means empty
# and 1 means not empty, and an integer n, return if n new flowers can be
# planted in the flowerbed without violating the no-adjacent-flowers rule.
# 
# 
# Example 1:
# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: true
# Example 2:
# Input: flowerbed = [1,0,0,0,1], n = 2
# Output: false
# 
# 
# Constraints:
# 
# 
# 1 <= flowerbed.length <= 2 * 10^4
# flowerbed[i] is 0 or 1.
# There are no two adjacent flowers in flowerbed.
# 0 <= n <= flowerbed.length
# 
# 
#

# @lc code=start
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        plant_loc = [i for i in range(len(flowerbed)) if flowerbed[i]==1]
        if not plant_loc:
            su = (len(flowerbed) + 1) // 2
        else:
            first_loc = plant_loc[0]
            last_loc = plant_loc[-1]
            su = 0
            su += first_loc // 2
            su += (len(flowerbed) - last_loc - 1) // 2
            if len(plant_loc) >= 2:
                for i in range(1, len(plant_loc)):
                    su += (plant_loc[i] - plant_loc[i-1]) // 2 - 1
        return su >= n
# @lc code=end

