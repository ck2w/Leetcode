
# Given an integer array nums, find the subarray with the largest sum, and return its sum.

# Kadane's算法的核心思想是动态规划中的局部最优决策：在遍历每个元素时，做一个贪心选择——
# 1.是把当前元素"接"到之前的子数组上
# 2.还是从当前元素重新开始？

def max_subarray(nums):
  current_sum = nums[0] # 以第一个元素初始化
  max_sum = nums[0]
  for i in range(1, len(nums)):
  	# 在每个位置只做一个选择：接上去/重新开始
  	# 接上去：current_sum + nums[i] > nums[i]，说明前面的和是"正贡献"，值得携带
	# 重新开始：nums[i] 更大，说明前面积累的和已经是负数了，从当前元素重起更优
    current_sum = max(nums[i], current_sum + nums[i])
    max_sum = max(max_sum, current_sum)
  return max_sum