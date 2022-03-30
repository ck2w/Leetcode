
# @lc app=leetcode id=2149 lang=python3
#
# [2149] Rearrange Array Elements by Sign
#
# @lc code=start
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        from collections import deque
        pos_q = deque()
        neg_q = deque()
        result = []
        for num in nums:
            if num > 0:
                pos_q.append(num)
            else:
                neg_q.append(num)
        while pos_q and neg_q:
            result.append(pos_q.popleft())
            result.append(neg_q.popleft())
        return result

# @lc code=end
