#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#
# https://leetcode.com/problems/sliding-window-maximum/description/
#
# algorithms
# Hard (44.66%)
# Likes:    5381
# Dislikes: 222
# Total Accepted:    377.4K
# Total Submissions: 844.9K
# Testcase Example:  '[1,3,-1,-3,5,3,6,7]\n3'
#
# You are given an array of integers nums, there is a sliding window of size k
# which is moving from the very left of the array to the very right. You can
# only see the k numbers in the window. Each time the sliding window moves
# right by one position.
# 
# Return the max sliding window.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]
# Explanation: 
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
# ⁠1 [3  -1  -3] 5  3  6  7       3
# ⁠1  3 [-1  -3  5] 3  6  7       5
# ⁠1  3  -1 [-3  5  3] 6  7       5
# ⁠1  3  -1  -3 [5  3  6] 7       6
# ⁠1  3  -1  -3  5 [3  6  7]      7
# 
# 
# Example 2:
# 
# 
# Input: nums = [1], k = 1
# Output: [1]
# 
# 
# Example 3:
# 
# 
# Input: nums = [1,-1], k = 1
# Output: [1,-1]
# 
# 
# Example 4:
# 
# 
# Input: nums = [9,11], k = 2
# Output: [11]
# 
# 
# Example 5:
# 
# 
# Input: nums = [4,-2], k = 2
# Output: [4]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
# 1 <= k <= nums.length
# 
# 
#

# @lc code=start
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # save index in deque
        
        from collections import deque

        q = deque()

        if len(nums) * k == 0:
            return []
        if k == 1:
            return nums

        def remove_smaller_num(i):
            # remove out-of-window index
            if q and i - k == q[0]:
                q.popleft()
            
            # remove smaller value index
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            
            # after this, values matching index in q are descreasing
        
        result = []

        for i in range(k):
            remove_smaller_num(i)
            q.append(i)
        result.append(nums[q[0]])

        for i in range(k, len(nums)):
            remove_smaller_num(i)
            q.append(i)
            result.append(nums[q[0]])

        return result


# @lc code=end

