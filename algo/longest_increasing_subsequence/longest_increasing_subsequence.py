def length_of_lis(nums):
    if not nums:
        return 0
    
    n = len(nums)
    dp = [1] * n  
    # base case：每个元素自身长度为1
    # 定义状态： dp[i] = 以 nums[i] 结尾的最长递增子序列长度。
    # 转移方程： dp[i] = max(dp[j] + 1)   对所有 j < i 且 nums[j] < nums[i]
    # 最终答案： max(dp)，因为最长子序列可以结尾在任意位置。
    
    for i in range(1, n):
        for j in range(i):              # 枚举所有 j < i
            if nums[j] < nums[i]:       # 可以接在 j 后面
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)

# 测试
nums = [10, 9, 2, 5, 3, 7, 101, 18]
print(length_of_lis(nums))  # 输出 4