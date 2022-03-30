
# @lc app=leetcode id=2138 lang=python3
#
# [2138] Divide a String Into Groups of Size k
#
# https://leetcode.com/problems/divide-a-string-into-groups-of-size-k/

# @lc code=start
class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        if not s:
            return [fill * k]
        
        group_num = len(s) // k
        res_num = len(s) % k
        
        result = []
        print(group_num, res_num)
        if group_num:
            for i in range(group_num):
                result.append(s[i*k:(i+1)*k])
            
            if res_num:
                result.append(s[(i+1)*k:] + fill * (k-res_num))
        else:
            result.append(s + fill * (k-res_num))
        
        return result
        
# @lc code=end
