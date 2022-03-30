
# @lc app=leetcode id=2165 lang=python3
#
# [2165] Smallest Value of the Rearranged Number

#
# @lc code=start
class Solution:
    def smallestNumber(self, num: int) -> int:        
        abs_val = abs(num)
        abs_val_str = str(abs_val)
        
        if num == 0:
            return 0
        elif num > 0:
            # get min except for 0

            digits = [int(x) for x in list(abs_val_str)]
            min_val = max(digits)
            for i in range(len(digits)):
                if digits[i] > 0 and digits[i] < min_val:
                    min_val = digits[i]            
            new_list = digits.copy()
            new_list.remove(min_val)
            new_list = [str(x) for x in new_list]
            result = str(min_val) + ''.join(sorted(new_list))
        elif num < 0:
            digits = [int(x) for x in list(abs_val_str)]
            sorted_digits = sorted(digits, reverse=True)
            result = '-'+ ''.join([str(x) for x in sorted_digits])
        return int(result)     

# @lc code=end
