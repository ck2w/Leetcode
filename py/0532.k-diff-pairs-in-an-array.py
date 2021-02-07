#
# @lc app=leetcode id=532 lang=python3
#
# [532] K-diff Pairs in an Array
#
# https://leetcode.com/problems/k-diff-pairs-in-an-array/description/
#
# algorithms
# Easy (31.81%)
# Likes:    698
# Dislikes: 1416
# Total Accepted:    113.7K
# Total Submissions: 357.1K
# Testcase Example:  '[3,1,4,1,5]\n2'
#
# 
# Given an array of integers and an integer k, you need to find the number of
# unique k-diff pairs in the array. Here a k-diff pair is defined as an integer
# pair (i, j), where i and j are both numbers in the array and their absolute
# difference is k.
# 
# 
# 
# Example 1:
# 
# Input: [3, 1, 4, 1, 5], k = 2
# Output: 2
# Explanation: There are two 2-diff pairs in the array, (1, 3) and (3,
# 5).Although we have two 1s in the input, we should only return the number of
# unique pairs.
# 
# 
# 
# Example 2:
# 
# Input:[1, 2, 3, 4, 5], k = 1
# Output: 4
# Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4)
# and (4, 5).
# 
# 
# 
# Example 3:
# 
# Input: [1, 3, 1, 5, 4], k = 0
# Output: 1
# Explanation: There is one 0-diff pair in the array, (1, 1).
# 
# 
# 
# Note:
# 
# The pairs (i, j) and (j, i) count as the same pair.
# The length of the array won't exceed 10,000.
# All the integers in the given input belong to the range: [-1e7, 1e7].
# 
# 
#

# @lc code=start

# 1 brutal force
# class Solution:
#     def findPairs(self, nums: List[int], k: int) -> int:
#         from collections import Counter
#         counter = Counter(nums)
#         is_pair = {}
        
#         if k==0:            
#             pair_count = 0
#             for x in counter:
#                 if counter[x] > 1:
#                     pair_count = pair_count + 1
#             return pair_count
#         elif k < 0:
#             return 0
#         else:                
#             for i in nums:                
#                 if i+k in nums: # the slowest step
#                     is_pair[str(i)+'-'+str(i+k)] = 1
#             return len(is_pair)

# 2 hash table (64ms)
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        from collections import Counter
        result = 0
        counter = Counter(nums)
        if k < 0:
            pass        
        for x in counter:
            if k > 0 and x + k in counter:
                result += 1
            elif k == 0 and counter[x] > 1:
                result += 1
        return result

# @lc code=end

