
# @lc app=leetcode id=2194 lang=python3
#
# [2194] 
#
# @lc code=start
class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        def get_split_loc(string):
            for i in range(len(string)):
                if string[i].isnumeric():
                    return i
            
        start_p, end_p = s.split(':')
        start_loc = get_split_loc(start_p)
        end_loc = get_split_loc(end_p)
        start_r, start_c = start_p[:start_loc], start_p[start_loc:]
        end_r, end_c = end_p[:end_loc], end_p[end_loc:]
        
        col_list = list(range(int(start_c), int(end_c)+1))
        row_list = list(range(ord(start_r), ord(end_r)+1))
        
        result = []
        for r in row_list:
            for c in col_list:        
                result.append(chr(r)+str(c))
        return result

# @lc code=end
