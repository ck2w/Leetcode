#
# @lc app=leetcode id=771 lang=python3
#
# [771] Jewels and Stones
#
# https://leetcode.com/problems/jewels-and-stones/description/
#
# algorithms
# Easy (87.52%)
# Likes:    3230
# Dislikes: 471
# Total Accepted:    701.9K
# Total Submissions: 802K
# Testcase Example:  '"aA"\n"aAAbbbb"'
#
# You're given strings jewels representing the types of stones that are jewels,
# and stones representing the stones you have. Each character in stones is a
# type of stone you have. You want to know how many of the stones you have are
# also jewels.
# 
# Letters are case sensitive, so "a" is considered a different type of stone
# from "A".
# 
# 
# Example 1:
# Input: jewels = "aA", stones = "aAAbbbb"
# Output: 3
# Example 2:
# Input: jewels = "z", stones = "ZZ"
# Output: 0
# 
# 
# Constraints:
# 
# 
# 1 <= jewels.length, stones.length <= 50
# jewels and stones consist of only English letters.
# All the characters of jewels are unique.
# 
# 
#

# @lc code=start
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        s = set(jewels)
        count = 0
        for i in stones:
            if i in s:
                count += 1
        return count

# @lc code=end

