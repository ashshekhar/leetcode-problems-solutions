#
# @lc app=leetcode id=778 lang=python
#
# [778] Swim in Rising Water
#

# @lc code=start
import heapq

class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # This problem is basically Djikstra's (BFS with min heap) to find the path that reaches the last grid with the smallest height encountered along path
        min_heap = []
        visited = set()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        rows = len(grid)
        cols = len(grid[0])
        
        min_heap.append((grid[0][0], 0, 0))
        visited.add((0, 0))
        
        while min_heap:
            max_path_val, row, col = heapq.heappop(min_heap)
            
            if row == rows - 1 and col == cols - 1:
                return max_path_val
            
            for direction in directions:
                new_r = direction[0] + row
                new_c = direction[1] + col
                
                if (new_r < 0 or new_r >= rows or new_c < 0 or new_c >= cols or (new_r, new_c) in visited):
                    continue
                else:
                    visited.add((new_r, new_c))
                    heapq.heappush(min_heap, max(max_path_val, grid[new_r][new_c]), new_r, new_c)
                
        return max_path_val
        
# @lc code=end

