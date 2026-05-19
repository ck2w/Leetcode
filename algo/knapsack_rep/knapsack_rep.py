def knapsack_with_repetition(W, weights, values):
    n = len(weights)
    dp = [0] * (W + 1)          # Base Case: dp[0] = 0

    for c in range(1, W + 1):   # 容量从小到大
        for i in range(n):
            if weights[i] <= c:
                dp[c] = max(dp[c], dp[c - weights[i]] + values[i])
                # 容量 c 的最优解，一定是"最后放入某个物品 i"之后得到的。

    return dp[W]                 # 最终答案