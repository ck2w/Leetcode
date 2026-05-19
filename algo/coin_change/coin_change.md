Coin Change — 
题目概括给定硬币面额数组和目标金额，求凑出该金额所需的最少硬币数，无法凑出返回 -1。无限供应每种硬币。


定义 dp[i] = 凑出金额 i 所需的最少硬币数。


- 状态转移方程
dp[i] = min(dp[i - coin] + 1)   for each coin in coins, if i >= coin

- base case
dp[0] = 0          # 金额为0，需要0枚硬币
dp[1..amount] = ∞  # 初始设为无穷大（代表"尚未可达"）