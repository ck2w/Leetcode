#
# @lc app=leetcode id=849 lang=python3
#
# [849] Maximize Distance to Closest Person
#
# https://leetcode.com/problems/maximize-distance-to-closest-person/description/
#
# algorithms
# Medium (44.73%)
# Likes:    2313
# Dislikes: 154
# Total Accepted:    155.4K
# Total Submissions: 330K
# Testcase Example:  '[1,0,0,0,1,0,1]'
#
# You are given an array representing a row of seats where seats[i] = 1
# represents a person sitting in the i^th seat, and seats[i] = 0 represents
# that the i^th seat is empty (0-indexed).
# 
# There is at least one empty seat, and at least one person sitting.
# 
# Alex wants to sit in the seat such that the distance between him and the
# closest person to him is maximized. 
# 
# Return that maximum distance to the closest person.
# 
# 
# Example 1:
# 
# 
# Input: seats = [1,0,0,0,1,0,1]
# Output: 2
# Explanation: 
# If Alex sits in the second open seat (i.e. seats[2]), then the closest person
# has distance 2.
# If Alex sits in any other open seat, the closest person has distance 1.
# Thus, the maximum distance to the closest person is 2.
# 
# 
# Example 2:
# 
# 
# Input: seats = [1,0,0,0]
# Output: 3
# Explanation: 
# If Alex sits in the last seat (i.e. seats[3]), the closest person is 3 seats
# away.
# This is the maximum distance possible, so the answer is 3.
# 
# 
# Example 3:
# 
# 
# Input: seats = [0,1]
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# 2 <= seats.length <= 2 * 10^4
# seats[i] is 0 or 1.
# At least one seat is empty.
# At least one seat is occupied.
# 
# 
#

# @lc code=start
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        first_loc = -1
        last_loc = -1
        n = len(seats)
        locs = []        

        for i in range(n):
            if seats[i] == 1:
                locs.append(i)
        first_loc = locs[0]
        last_loc = locs[-1]

        distances = [first_loc, n-last_loc-1]
        for i in range(1, len(locs)):
            diff = locs[i] - locs[i-1]
            distances.append(diff // 2)
        
        return max(distances)
        
# @lc code=end

