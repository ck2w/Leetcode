
# 问题
- 给定一个无重复整数数组 candidates 和目标值 target，找出所有相加之和等于 target 的组合。
- 规则：
- 每个数字可以无限次重复使用
- 结果不能有重复组合（[2,3] 和 [3,2] 视为同一个）
- 例： candidates = [2,3,6,7]，target = 7 → [[2,2,3],[7]]


# 状态定义
- dp[s] = 所有和恰好等于 s 的组合列表（每个组合是一个数组）
- dp[s] 是一个列表的列表（list of lists）
- 例如 dp[7] = [[2,2,3], [7]] 表示和为7的所有组合

# 转移方程
- dp[s] = 对每个候选数x，把dp[s-x]中每个组合追加x，合并所有结果
- dp[s] += [comb + [x] for comb in dp[s - x]]  (for each x in candidates)
```
for x in candidates:          # 固定当前候选数
    for s in range(x, target+1):   # 从小到大更新
        for comb in dp[s-x]:
            dp[s].append(comb + [x])
```
# base case
- dp[0] = [[]]   # 和为0的唯一组合：空组合


# 最终答案
- dp[target]