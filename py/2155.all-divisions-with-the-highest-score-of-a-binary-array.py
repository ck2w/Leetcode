
# @lc app=leetcode id=2155 lang=python3
#
# [2155] All Divisions With the Highest Score of a Binary Array
#
# @lc code=start
class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        total_score = sum(nums)
        max_score = total_score
        score_dict = {max_score: [0]}
        for i in range(1, len(nums)+1):
            if nums[i-1] == 0:
                total_score += 1
            elif nums[i-1] == 1:
                total_score -= 1
            if total_score == max_score:
                score_dict[max_score].append(i)
            elif total_score > max_score:
                max_score = total_score
                score_dict[max_score] = [i]
        return score_dict[max_score]     

# @lc code=end
