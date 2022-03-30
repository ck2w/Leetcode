#
# @lc app=leetcode id=374 lang=python3
#
# [374] Guess Number Higher or Lower
#
# https://leetcode.com/problems/guess-number-higher-or-lower/description/
#
# algorithms
# Easy (48.04%)
# Likes:    539
# Dislikes: 92
# Total Accepted:    273.1K
# Total Submissions: 568.5K
# Testcase Example:  '10\n6'
#
# We are playing the Guess Game. The game is as follows:
# 
# I pick a number from 1 to n. You have to guess which number I picked.
# 
# Every time you guess wrong, I will tell you whether the number I picked is
# higher or lower than your guess.
# 
# You call a pre-defined API int guess(int num), which returns 3 possible
# results:
# 
# 
# -1: The number I picked is lower than your guess (i.e. pick < num).
# 1: The number I picked is higher than your guess (i.e. pick > num).
# 0: The number I picked is equal to your guess (i.e. pick == num).
# 
# 
# Return the number that I picked.
# 
# 
# Example 1:
# 
# 
# Input: n = 10, pick = 6
# Output: 6
# 
# 
# Example 2:
# 
# 
# Input: n = 1, pick = 1
# Output: 1
# 
# 
# Example 3:
# 
# 
# Input: n = 2, pick = 1
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 2^31 - 1
# 1 <= pick <= n
# 
# 
#

# @lc code=start
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        lo = 1
        hi = n
        while lo <= hi:
            mid = (lo + hi) // 2
            guess_result = guess(mid)
            if guess_result == 0:
                return mid
            elif guess_result == 1:
                lo = mid + 1
            else:
                hi = mid - 1            
        return -1
            
# @lc code=end

