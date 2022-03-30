#
# @lc app=leetcode id=249 lang=python3
#
# [249] Group Shifted Strings
#
# @lc code=start
class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        d = {}
        for string in strings:
            # map function
            ords = [ord(i) for i in string]
            if len(ords) > 1:
                key = ''.join([str((t-ords[0]) % 26).zfill(2) for t in ords[1:]])
            else:
                key = '0'
                
            if key in d:
                d[key].append(string)
            else:
                d[key] = [string]
            print(key)
        return list(d.values())
            
# @lc code=end

