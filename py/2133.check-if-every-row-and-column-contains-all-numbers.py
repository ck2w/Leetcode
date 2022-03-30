
# @lc app=leetcode id=2133 lang=python3
#
# [2133] Check if Every Row and Column Contains All Numbers
#
# https://leetcode.com/problems/check-if-every-row-and-column-contains-all-numbers/
#
# @lc code=start
class Solution:
    class Solution:
        def checkValid(self, matrix: List[List[int]]) -> bool:
            n = len(matrix)
            
            def check_all_number(line):
                d = {k: 0 for k in range(1, n+1)}
                
                for num in line:
                    if num in d:
                        d[num] += 1
                    else:
                        return False
                for v in d.values():
                    if v == 1:
                        continue
                    else:
                        return False
                return True
            
            for i in range(n):
                line = matrix[i]

                if not check_all_number(line):
                    return False
                
                line = [x[i] for x in matrix]
                if not check_all_number(line):
                    return False
            
            return True
# @lc code=end
