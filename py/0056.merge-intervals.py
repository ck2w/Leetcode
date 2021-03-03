#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#
# https://leetcode.com/problems/merge-intervals/description/
#
# algorithms
# Medium (41.00%)
# Likes:    6574
# Dislikes: 361
# Total Accepted:    817.9K
# Total Submissions: 2M
# Testcase Example:  '[[1,3],[2,6],[8,10],[15,18]]'
#
# Given an array of intervals where intervals[i] = [starti, endi], merge all
# overlapping intervals, and return an array of the non-overlapping intervals
# that cover all the intervals in the input.
# 
# 
# Example 1:
# 
# 
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into
# [1,6].
# 
# 
# Example 2:
# 
# 
# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= intervals.length <= 10^4
# intervals[i].length == 2
# 0 <= starti <= endi <= 10^4
# 
# 
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals
        # sort
        sort_intervals = sorted(intervals)
        result = []

        start_pt = sort_intervals[0][0]
        end_pt = sort_intervals[0][1]

        for itv in sort_intervals[1:]:
            if itv[0] <= end_pt:
                # merge
                end_pt = max(end_pt, itv[1])
            else:
                # not merge
                result.append([start_pt, end_pt])
                start_pt = itv[0]
                end_pt = itv[1]
        result.append([start_pt, end_pt])
        return result
        
# @lc code=end

