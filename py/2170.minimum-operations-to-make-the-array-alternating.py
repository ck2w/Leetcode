
# @lc app=leetcode id=2170 lang=python3
#
# [2170] Minimum Operations to Make the Array Alternating
#
# @lc code=start
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:        
        n = len(nums)
        if n <= 1:
            return 0
        from collections import Counter
        # 1
        num1 = nums[::2]
        num2 = nums[1::2]
        n1 = len(num1)
        n2 = len(num2)
        
        c1 = Counter(num1)
        mode1 = c1.most_common(1)[0][0]
        if len(c1) > 1:
            mode12_num = c1.most_common(2)[1][1]
        else:
            mode12_num = 0
            
        op1 = len(num1) - c1[mode1]
        
        c2 = Counter(num2)
        mode2 = c2.most_common(1)[0][0]
        if len(c2) > 1:
            mode22_num = c2.most_common(2)[1][1]
        else:
            mode22_num = 0
        
        if mode1 != mode2:            
            operations = n1 - c1[mode1] + n2 - c2[mode2]            
        elif mode1 == mode2:
            # flip 1 to 2nd largest
            op1 = (n1 - mode12_num) + (n2 - c2[mode2])
            op2 = (n2 - mode22_num) + (n1 - c1[mode1])
            operations = min(op1, op2)
        return operations
# @lc code=end
