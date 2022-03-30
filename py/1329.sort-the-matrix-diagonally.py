#
# @lc app=leetcode id=1329 lang=python3
#
# [1329] Sort the Matrix Diagonally
#
# https://leetcode.com/problems/sort-the-matrix-diagonally/description/
#
# algorithms
# Medium (81.41%)
# Likes:    1415
# Dislikes: 171
# Total Accepted:    76.5K
# Total Submissions: 93.9K
# Testcase Example:  '[[3,3,1,1],[2,2,1,2],[1,1,1,2]]'
#
# A matrix diagonal is a diagonal line of cells starting from some cell in
# either the topmost row or leftmost column and going in the bottom-right
# direction until reaching the matrix's end. For example, the matrix diagonal
# starting from mat[2][0], where mat is a 6 x 3 matrix, includes cells
# mat[2][0], mat[3][1], and mat[4][2].
# 
# Given an m x n matrix mat of integers, sort each matrix diagonal in ascending
# order and return the resulting matrix.
# 
# 
# Example 1:
# 
# 
# Input: mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
# Output: [[1,1,1,1],[1,2,2,2],[1,2,3,3]]
# 
# 
# Example 2:
# 
# 
# Input: mat =
# [[11,25,66,1,69,7],[23,55,17,45,15,52],[75,31,36,44,58,8],[22,27,33,25,68,4],[84,28,14,11,5,50]]
# Output:
# [[5,17,4,1,52,7],[11,11,25,45,8,69],[14,23,25,44,58,15],[22,27,31,36,50,66],[84,28,75,33,55,68]]
# 
# 
# 
# Constraints:
# 
# 
# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 100
# 1 <= mat[i][j] <= 100
# 
# 
#

# @lc code=start
class Solution:
    # def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
    #     if not mat:
    #         return None
    #     m = len(mat)
    #     n = len(mat[0])

    #     # sort left side
    #     def helper(length, method='row'):
    #         for i in range(length):
    #             loc_lst = []
    #             num_lst = []            
    #             if method == 'row':
    #                 row, col = i, 0                    
    #             elif method == 'col':
    #                 row, col = 0, i

    #             # get diagonal elements locs and numbers
    #             while row < m and col < n:
    #                 loc_lst.append((row, col)) 
    #                 num_lst.append(mat[row][col])
    #                 row += 1
    #                 col += 1

    #             # sort diagonal values
    #             num_lst = sorted(num_lst)

    #             # fill diagonal elements
    #             for j in range(len(num_lst)):
    #                 row, col = loc_lst[j]
    #                 mat[row][col] = num_lst[j]
    #     helper(m, 'row')
    #     helper(n, 'col')
    #     return mat


    # use dict to store diagonal, key=row-col, value=list to store diagonal elements
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        d = {}
        
        rows = len(mat)
        cols = len(mat[0])

        for i in range(rows):
            for j in range(cols):
                if i-j in d:
                    d[i-j].append(mat[i][j])
                else:
                    d[i-j] = [mat[i][j]]
                    
        for v in d.values():
            v.sort(reverse=True)
            
        for i in range(rows):
            for j in range(cols):
                mat[i][j] = d[i-j].pop()
                
        return mat

# @lc code=end

