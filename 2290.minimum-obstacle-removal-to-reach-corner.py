#
# @lc app=leetcode id=2290 lang=python
#
# [2290] Minimum Obstacle Removal to Reach Corner
#

# @lc code=start
from collections import deque
import heapq

class Solution(object):
    def minimumObstacles(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # Since this is not a shortest path but minimum count, Djikstra's is optimal instead of simple BFS
        rows = len(grid)
        cols = len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        # Obstacle count, row, col
        min_heap = []
        heapq.heappush(min_heap, (0, 0, 0))
        
        visited = set([(0, 0)])
        
        # Djikstra's: BFS + Min_heap
        while min_heap:
            obs_count, row, col = heapq.heappop(min_heap)

            if row == rows -1 and col == cols - 1:
                return obs_count
            
            for direction in directions:
                new_row = row + direction[0]
                new_col = col + direction[1]
                
                if (0 <= new_row < rows and 0 <= new_col < cols) and (new_row, new_col) not in visited:
                    visited.add((new_row, new_col))
                    
                    new_obs_count = obs_count + grid[new_row][new_col]
                    
                    heapq.heappush(min_heap, (new_obs_count, new_row, new_col))
        
        return -1 
        
# @lc code=end

