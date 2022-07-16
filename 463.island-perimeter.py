#
# @lc app=leetcode id=463 lang=python
#
# [463] Island Perimeter
#

# @lc code=start
class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols  = len(grid[0])
        visited = set()
        
        # Since only one island
        global res
        res = 0
        
        
        def dfs(row, col):
            global res
            
            if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == 0:
                res += 1
                return
            
            if (row, col) in visited:
                return

            visited.add((row, col))
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            
            for direction in directions:
                dfs(row + direction[0], col + direction[1])
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    dfs(i, j)
        
        return res
            
# @lc code=end

