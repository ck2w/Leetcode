def lcs(X, Y):
    m, n = len(X), len(Y)
    
    # 建表
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # 填表
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i-1] == Y[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    # 回溯得到具体子序列,具体是哪些字符
    result = []
    i, j = m, n
    while i > 0 and j > 0:
        if X[i-1] == Y[j-1]:
            result.append(X[i-1])
            i -= 1; j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1
    
    return dp[m][n], ''.join(reversed(result))


# 测试
X, Y = "ABCBDAB", "BDCAB"
length, seq = lcs(X, Y)
print(f"长度: {length}")   # 4
print(f"LCS:  {seq}")      # BCAB