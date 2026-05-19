def matrix_chain_order(p):
    n = len(p) - 1
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    split = [[0] * (n + 1) for _ in range(n + 1)]

    for length in range(2, n + 1):
        for i in range(1, n - length + 2):
            j = i + length - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                cost = dp[i][k] + dp[k+1][j] + p[i-1] * p[k] * p[j]
                if cost < dp[i][j]:
                    dp[i][j] = cost
                    split[i][j] = k

    return dp, split


def print_optimal_parens(split, i, j):
    if i == j:
        return f"A{i}"
    k = split[i][j]
    left = print_optimal_parens(split, i, k)
    right = print_optimal_parens(split, k + 1, j)
    return f"({left} x {right})"


if __name__ == "__main__":
    p = [30, 35, 15, 5, 10, 20]  # 5个矩阵：30x35, 35x15, 15x5, 5x10, 10x20

    dp, split = matrix_chain_order(p)
    n = len(p) - 1

    print(f"最小乘法次数: {dp[1][n]}")
    print(f"最优括号方案: {print_optimal_parens(split, 1, n)}")