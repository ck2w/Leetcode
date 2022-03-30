#
# @lc app=leetcode id=599 lang=python3
#
# [599] Minimum Index Sum of Two Lists
#
# https://leetcode.com/problems/minimum-index-sum-of-two-lists/description/
#
# algorithms
# Easy (52.37%)
# Likes:    1050
# Dislikes: 302
# Total Accepted:    137.9K
# Total Submissions: 260.5K
# Testcase Example:  '["Shogun","Tapioca Express","Burger King","KFC"]\n["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]'
#
# Suppose Andy and Doris want to choose a restaurant for dinner, and they both
# have a list of favorite restaurants represented by strings.
# 
# You need to help them find out their common interest with the least list
# index sum. If there is a choice tie between answers, output all of them with
# no order requirement. You could assume there always exists an answer.
# 
# 
# Example 1:
# 
# 
# Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 =
# ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
# Output: ["Shogun"]
# Explanation: The only restaurant they both like is "Shogun".
# 
# 
# Example 2:
# 
# 
# Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 =
# ["KFC","Shogun","Burger King"]
# Output: ["Shogun"]
# Explanation: The restaurant they both like and have the least index sum is
# "Shogun" with index sum 1 (0+1).
# 
# 
# 
# Constraints:
# 
# 
# 1 <= list1.length, list2.length <= 1000
# 1 <= list1[i].length, list2[i].length <= 30
# list1[i] and list2[i] consist of spaces ' ' and English letters.
# All the stings of list1 are unique.
# All the stings of list2 are unique.
# 
# 
#

# @lc code=start
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        d1 = {list1[i]:i for i in range(len(list1))}
        d2 = {list2[i]:i for i in range(len(list2))}
        result = {}
        for k, v in d1.items():
            if k in d2:
                index_sum = d1[k] + d2[k]
                if index_sum in result:
                    result[index_sum].append(k)
                else:
                    result[index_sum] = [k]
        min_index = min(result.keys())
        return result[min_index]
# @lc code=end

