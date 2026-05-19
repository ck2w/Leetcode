
# 矩阵链乘法（Matrix Chain Multiplication）
- 给定 n 个矩阵的链，在不改变顺序的前提下，通过加括号决定计算顺序，使得总标量乘法次数最少。

# 定义状态
- dp[i][j] = 计算矩阵链 Aᵢ × Aᵢ₊₁ × ··· × Aⱼ 所需的最少标量乘法次数。

# 转移方程
- dp[i][j] = min (over k from i to j-1 of : dp[i][k] + dp[k+1][j] + p[i-1] * p[k] * p[j])

# Base Case
- dp[i][i]=0，单个矩阵无需任何乘法。

# 最终答案
- dp[1][n]