
# @lc app=leetcode id=2150 lang=python3
#
# [2150] Find All Lonely Numbers in the Array
#
# @lc code=start

class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        from collections import Counter
        c = Counter(nums)
        keys = c.keys()
        result = []
        for k in keys:
            if (c[k] == 1) and (k+1 not in c) and (k-1 not in c):
                result.append(k)
        return result

# @lc code=end
