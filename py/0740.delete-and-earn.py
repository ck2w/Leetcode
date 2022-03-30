#
# @lc app=leetcode id=740 lang=python3
#
# [740] Delete and Earn
#
# https://leetcode.com/problems/delete-and-earn/description/
#
# algorithms
# Medium (54.52%)
# Likes:    3044
# Dislikes: 198
# Total Accepted:    111.5K
# Total Submissions: 204.3K
# Testcase Example:  '[3,4,2]'
#
# You are given an integer array nums. You want to maximize the number of
# points you get by performing the following operation any number of
# times:
# 
# 
# Pick any nums[i] and delete it to earn nums[i] points. Afterwards, you must
# delete every element equal to nums[i] - 1 and every element equal to nums[i]
# + 1.
# 
# 
# Return the maximum number of points you can earn by applying the above
# operation some number of times.
# 
# 
# Example 1:
# 
# 
# Input: nums = [3,4,2]
# Output: 6
# Explanation: You can perform the following operations:
# - Delete 4 to earn 4 points. Consequently, 3 is also deleted. nums = [2].
# - Delete 2 to earn 2 points. nums = [].
# You earn a total of 6 points.
# 
# 
# Example 2:
# 
# 
# Input: nums = [2,2,3,3,3,4]
# Output: 9
# Explanation: You can perform the following operations:
# - Delete a 3 to earn 3 points. All 2's and 4's are also deleted. nums =
# [3,3].
# - Delete a 3 again to earn 3 points. nums = [3].
# - Delete a 3 once more to earn 3 points. nums = [].
# You earn a total of 9 points.
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 2 * 10^4
# 1 <= nums[i] <= 10^4
# 
# 
#

# @lc code=start
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        from collections import Counter
        c = Counter(nums)
        lst = sorted(list(c.keys()))
        vals_dict = {k: k * c[k] for k in lst}

        n = len(lst)
        dp = [0] * len(lst)
        for i in range(n-1, -1, -1):
            if i == n-1:
                dp[i] = vals_dict[lst[i]]
            elif i == n-2:
                if lst[i+1] - lst[i] > 1:
                    # take last two
                    dp[i] = vals_dict[lst[i]] + dp[i+1]
                else:
                    # take larger one of last two
                    dp[i] = max(vals_dict[lst[i]], dp[i+1])
            else:                
                if lst[i+1] - lst[i] > 1:
                    # take this and this.next
                    dp[i] = vals_dict[lst[i]] + dp[i+1]
                else:
                    # 1.take this and this.next.next
                    # 2.or take take.next
                    dp[i] = max(vals_dict[lst[i]] + dp[i+2], dp[i+1])
        return dp[0]

# @lc code=end

