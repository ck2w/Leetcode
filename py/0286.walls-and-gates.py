

# @lc app=leetcode id=286 lang=python3

# @lc code=start

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        from collections import deque
        m = len(rooms)
        n = len(rooms[0])
        GATE = 0
        EMPTY = 2147483647
        
        move_up = [0, 1]
        move_down = [0, -1]
        move_left = [-1, 0]
        move_right = [1, 0]
        moves = [move_up, move_down, move_left, move_right]
        
        q = deque()
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == GATE:                    
                    q.append([i, j])
                    
        while q:
            point = q.popleft()
            for move in moves:                
                r = point[0] + move[0]
                c = point[1] + move[1]
                if r < 0 or r >= m or c < 0 or c >= n or rooms[r][c] != EMPTY:
                    continue
                rooms[r][c] = rooms[point[0]][point[1]] + 1
                q.append([r, c])

        
# @lc code=end
