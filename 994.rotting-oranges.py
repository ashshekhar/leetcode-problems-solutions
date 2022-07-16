#
# @lc app=leetcode id=994 lang=python
#
# [994] Rotting Oranges
#

# @lc code=start
from collections import deque

class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """  
        # DFS approach like 01 Matrix won't work because you can be given multiple rotten oranges
        # Multi source BFS works
        queue = deque()
        
        rows = len(grid)
        cols = len(grid[0])
        
        fresh = 0
        time = 0
        directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        
        # Count number of fresh oranges and add rotten to queue
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    queue.appendleft([i, j])
        
        # Outer while loop runs once for all rotten oranges at the same time
        while queue and fresh > 0:
            
            # This is to make sure time += 1 happens after one rotting session
            for i in range(len(queue)):
                row, col = queue.pop()
                
                for direction in directions:
                    new_row, new_col = row + direction[0], col + direction[1]
                    
                    if new_row > rows - 1 or new_row < 0 or new_col < 0 or new_col > cols - 1 or grid[new_row][new_col] != 1:
                        continue
                    
                    # Mark as rotten and append to queue for future
                    grid[new_row][new_col] = 2
                    fresh -= 1
                    queue.appendleft([new_row, new_col])
                    
            time += 1
                    
        if fresh > 0:
            return -1
        return time
# @lc code=end

