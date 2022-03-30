
# @lc app=leetcode id=2195 lang=python3
#
# [2195] 
#
# @lc code=start
class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:

        total_val = 0
        nums_sorted = sorted(list(set(nums)))
        if 1 not in nums_sorted:
            nums_sorted = [1] + nums_sorted
            k = k - 1
            total_val += 1           
            
        start_p = nums_sorted[0]        
        for i in nums_sorted[1:]:
            
            if k == 0:
                break                
            consume_k = i - start_p - 1            
            if consume_k < k:
                k = k - consume_k
                start_p = start_p + 1
                end_p = i - 1
                total_val += (start_p + end_p) * consume_k // 2
            else:                
                start_p = start_p + 1
                end_p = start_p + k - 1
                total_val += (start_p + end_p) * k // 2
                k = 0                        
            start_p = i 
        if k > 0:
            start_p = nums_sorted[-1] + 1
            end_p = nums_sorted[-1] + k            
            total_val += (start_p + end_p) * k // 2            
            
        return total_val

# @lc code=end
