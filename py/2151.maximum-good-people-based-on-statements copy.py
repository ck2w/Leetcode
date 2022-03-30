
# @lc app=leetcode id=2151 lang=python3
#
# [2151] Maximum Good People Based on Statements
#
# @lc code=start
class Solution:
    def maximumGood(self, statements: List[List[int]]) -> int:
        # brute force
        # 1: dfs traver possible combination        
        
        n = len(statements)
        stack = [[1], [0]]
        combinations = []
        while stack:
            comb = stack.pop()
            if len(comb) == n:
                combinations.append(comb)
            else:
                stack.append(comb + [0])
                stack.append(comb + [1])
        
        # 2: check if valid
        max_val = 0
        for state in combinations:
            valid = True
            for i in range(n):
                if state[i] == 0:
                    # ignore bad person's statement
                    continue
                elif state[i] == 1:
                    for j in range(n):
                        if state[j] == 1 and statements[i][j] == 0:
                            valid = False
                            break
                        elif state[j] == 0 and statements[i][j] == 1:
                            valid = False
                            break                            
                            
            if valid:            
                max_val = max(max_val, sum(state))
        return max_val            
            

# @lc code=end
