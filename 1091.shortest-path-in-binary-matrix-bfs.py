#
# @lc app=leetcode id=1091 lang=python
#
# [1091] Shortest Path in Binary Matrix
#

# @lc code=start
from collections import deque

class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        
        # 8 Directionally connected
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1], 
                      [-1, -1], [-1, 1], [1, -1], [1, 1]]
        q = deque()
        visited = set()
        
        def bfs(i, j):
            if i < 0 or i > rows - 1 or j < 0 or j > cols - 1:
                return
            
            visited.add((i, j))
            q.append((i, j, 0))
            
            while q:
                row, col, count = q.popleft()
                
                if grid[row][col] == 0 and row == rows - 1 and col == cols - 1:
                    return count + 1
                
                for direction in directions:
                    new_row, new_col = row + direction[0], col + direction[1]
                    
                    if new_row < 0 or new_row > rows- 1 or new_col < 0 or new_col > cols - 1 or grid[new_row][new_col] == 1:
                        continue
                    
                    if (new_row, new_col) not in visited:
                        visited.add((new_row, new_col))
                        q.append((new_row, new_col, count + 1))
            return -1
        
        
        if grid[0][0] == 0 and grid[rows - 1][cols - 1] == 0:
            return bfs(0, 0)
        
        return -1
# @lc code=end

