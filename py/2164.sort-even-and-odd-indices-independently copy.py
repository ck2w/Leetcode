
# @lc app=leetcode id=2164 lang=python3
#
# [2164] Sort Even and Odd Indices Independently
#
# @lc code=start
class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        odd_num = sorted(nums[1::2])
        even_num = sorted(nums[0::2], reverse=True)
        result = []
        while even_num:
            result.append(even_num.pop())
            if odd_num:
                result.append(odd_num.pop())
        return result      

# @lc code=end
