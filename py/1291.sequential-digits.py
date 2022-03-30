#
# @lc app=leetcode id=1291 lang=python3
#
# [1291] Sequential Digits
#
# https://leetcode.com/problems/sequential-digits/description/
#
# algorithms
# Medium (57.50%)
# Likes:    861
# Dislikes: 67
# Total Accepted:    48.5K
# Total Submissions: 82.5K
# Testcase Example:  '100\n300'
#
# An integer has sequential digits if and only if each digit in the number is
# one more than the previous digit.
# 
# Return a sorted list of all the integers in the range [low, high] inclusive
# that have sequential digits.
# 
# 
# Example 1:
# Input: low = 100, high = 300
# Output: [123,234]
# Example 2:
# Input: low = 1000, high = 13000
# Output: [1234,2345,3456,4567,5678,6789,12345]
# 
# 
# Constraints:
# 
# 
# 10 <= low <= high <= 10^9
# 
# 
#

# @lc code=start
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        n = len(sample)
        result = []
        for i in range(n):
            for j in range(i+1, n+1):
                num = int(sample[i:j])
                if low <= num <= high:
                    result.append(num)     
        return sorted(result)
                
# @lc code=end

