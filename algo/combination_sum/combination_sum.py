class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = [[] for _ in range(target + 1)]
        dp[0] = [[]]

        # 转移方程
		# dp[s] = 对每个候选数x，把dp[s-x]中每个组合追加x，合并所有结果
		# dp[s] += [comb + [x] for comb in dp[s - x]]  (for each x in candidates)
        for x in candidates:
            for s in range(x, target + 1):
                for comb in dp[s - x]:
                    dp[s].append(comb + [x])

        return dp[target]