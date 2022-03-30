
# @lc app=leetcode id=2156 lang=python
#
# [2156] Find Substring With Given Hash Value
#
# @lc code=start
class Solution(object):
    def subStrHash(self, s, power, modulo, k, hashValue):
        """
        :type s: str
        :type power: int
        :type modulo: int
        :type k: int
        :type hashValue: int
        :rtype: str
        """
        val = {chr(i): i-96 for i in range(97, 123)}

        from collections import deque
        q = deque(maxlen=k)
        window_sum = 0
        power_base = 1
        for i in range(k):
            new_letter = s[i]
            q.append(new_letter)            
            window_sum += val[new_letter] * power_base
            power_base *= power

        modulo_result = window_sum % modulo
        if modulo_result == hashValue:
            return s[:k]
            
        
        new_multiplier = power ** (k-1) 
        for i in range(k, len(s)):
            new_letter = s[i]
            old_val = val[q.popleft()]
            new_val = val[new_letter] * new_multiplier
            window_sum = (window_sum - old_val)//power + new_val
            q.append(new_letter)
            
            if window_sum % modulo == hashValue:
                break

        result = ''.join(list(q))
        
        return result        

# @lc code=end
