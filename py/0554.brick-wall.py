#
# @lc app=leetcode id=554 lang=python3
#
# [554] Brick Wall
#
# https://leetcode.com/problems/brick-wall/description/
#
# algorithms
# Medium (51.81%)
# Likes:    1513
# Dislikes: 75
# Total Accepted:    89.5K
# Total Submissions: 172.7K
# Testcase Example:  '[[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]'
#
# There is a rectangular brick wall in front of you with n rows of bricks. The
# i^th row has some number of bricks each of the same height (i.e., one unit)
# but they can be of different widths. The total width of each row is the
# same.
# 
# Draw a vertical line from the top to the bottom and cross the least bricks.
# If your line goes through the edge of a brick, then the brick is not
# considered as crossed. You cannot draw a line just along one of the two
# vertical edges of the wall, in which case the line will obviously cross no
# bricks.
# 
# Given the 2D array wall that contains the information about the wall, return
# the minimum number of crossed bricks after drawing such a vertical line.
# 
# 
# Example 1:
# 
# 
# Input: wall = [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: wall = [[1],[1],[1]]
# Output: 3
# 
# 
# 
# Constraints:
# 
# 
# n == wall.length
# 1 <= n <= 10^4
# 1 <= wall[i].length <= 10^4
# 1 <= sum(wall[i].length) <= 2 * 10^4
# sum(wall[i]) is the same for each row i.
# 1 <= wall[i][j] <= 2^31 - 1
# 
# 
#

# @lc code=start
from typing import Counter


class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        def cumsum(lst):
            for i in range(len(lst)):
                if i == 0:
                    pass
                else:
                    lst[i] = lst[i] + lst[i-1]
            return lst
        from collections import Counter
        from functools import reduce

        if not wall: return 0        

        wall_num = len(wall)
        wall_len = sum(wall[0])
        c = reduce(lambda x, y: x+y, [Counter(cumsum(i)) for i in wall])
        del c[wall_num]
        del c[wall_len]
        if c:
            return wall_num - c.most_common(1)[0][1]
        else:
            return wall_num
# @lc code=end

