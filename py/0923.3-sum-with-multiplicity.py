#
# @lc app=leetcode id=923 lang=python3
#
# [923] 3Sum With Multiplicity
#
# https://leetcode.com/problems/3sum-with-multiplicity/description/
#
# algorithms
# Medium (36.31%)
# Likes:    535
# Dislikes: 95
# Total Accepted:    27.5K
# Total Submissions: 72.1K
# Testcase Example:  '[1,1,2,2,3,3,4,4,5,5]\n8'
#
# Given an integer array arr, and an integer target, return the number of
# tuples i, j, k such that i < j < k and arr[i] + arr[j] + arr[k] == target.
# 
# As the answer can be very large, return it modulo 10^9 + 7.
# 
# 
# Example 1:
# 
# 
# Input: arr = [1,1,2,2,3,3,4,4,5,5], target = 8
# Output: 20
# Explanation: 
# Enumerating by the values (arr[i], arr[j], arr[k]):
# (1, 2, 5) occurs 8 times;
# (1, 3, 4) occurs 8 times;
# (2, 2, 4) occurs 2 times;
# (2, 3, 3) occurs 2 times.
# 
# 
# Example 2:
# 
# 
# Input: arr = [1,1,2,2,2,2], target = 5
# Output: 12
# Explanation: 
# arr[i] = 1, arr[j] = arr[k] = 2 occurs 12 times:
# We choose one 1 from [1,1] in 2 ways,
# and two 2s from [2,2,2,2] in 6 ways.
# 
# 
# 
# Constraints:
# 
# 
# 3 <= arr.length <= 3000
# 0 <= arr[i] <= 100
# 0 <= target <= 300
# 
# 
#

# @lc code=start
class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        from collections import Counter

        MOD = 10**9 + 7
        count = Counter(arr)
        
        ans = 0

        # assume: x<=y<=z

        # All different
        # x<y<z
        for x in range(0, 101):
            for y in range(x+1, 101):
                z = target - x - y
                if y < z <= 100:
                    ans += count[x] * count[y] * count[z]
                    ans %= MOD

        # x == y
        # num = C(n,2) * count[z]
        # C(n,2) = n*(n-1)/2, n = count[x]
        for x in range(0, 101):
            z = target - 2*x
            if x < z <= 100:
                ans += count[x] * (count[x] - 1) / 2 * count[z]
                ans %= MOD

        # y == z
        # num = C(n,2) * count[x]
        # C(n,2) = n*(n-1)/2, n = count[y]
        for x in range(0, 101):
            if (target - x) % 2 == 0:
                y = (target - x) / 2
                if x < y <= 100:
                    ans += count[x] * count[y] * (count[y] - 1) / 2
                    ans %= MOD

        # x == y == z
        # num = C(n,3) = n * (n-1) * (n-2) / 6, n = count[x]
        if target % 3 == 0:
            x = target / 3
            if 0 <= x <= 100:
                ans += count[x] * (count[x] - 1) * (count[x] - 2) / 6
                ans %= MOD

        return int(ans)
# @lc code=end

