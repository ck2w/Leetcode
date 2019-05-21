#
# @lc app=leetcode id=1002 lang=python3
#
# [1002] Find Common Characters
#
# https://leetcode.com/problems/find-common-characters/description/
#
# algorithms
# Easy (66.02%)
# Likes:    216
# Dislikes: 34
# Total Accepted:    19.6K
# Total Submissions: 29.8K
# Testcase Example:  '["bella","label","roller"]'
#
# Given an array A of strings made only from lowercase letters, return a list
# of all characters that show up in all strings within the list (including
# duplicates).  For example, if a character occurs 3 times in all strings but
# not 4 times, you need to include that character three times in the final
# answer.
# 
# You may return the answer in any order.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: ["bella","label","roller"]
# Output: ["e","l","l"]
# 
# 
# 
# Example 2:
# 
# 
# Input: ["cool","lock","cook"]
# Output: ["c","o"]
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= A.length <= 100
# 1 <= A[i].length <= 100
# A[i][j] is a lowercase letter
# 
# 
# 
# 1 orderded dictionary (52 ms)
# class Solution:
#     def commonChars(self, A: List[str]) -> List[str]:
#         from collections import OrderedDict
#         d = OrderedDict()
#         for letter in A[0]:
#             if letter in d:
#                 d[letter] += 1
#             else:
#                 d[letter] = 1        

#         for i in A[1:]:
#             new_d = {}
#             for letter in i:
#                 if letter in d:
#                     if letter in new_d:
#                         new_d[letter] += 1
#                     else:
#                         new_d[letter] = 1
#             for key in list(d.keys()):
#                 if key in new_d:
#                     d[key] = min(d[key], new_d[key])
#                 else:
#                     del d[key]            
#         result = []
#         for key, value in d.items():
#             result.extend([key]*value)
#         return result


# 2 Counter (56 ms)
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        from collections import Counter
        res = Counter(A[0])
        for a in A:
            res &= Counter(a)
        return list(res.elements())

