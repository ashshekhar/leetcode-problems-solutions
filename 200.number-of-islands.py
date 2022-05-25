#
# @lc app=leetcode id=200 lang=python
#
# [200] Number of Islands
#

# @lc code=start
class Solution(object):
    def mark_visited(self, grid, rows, columns, i, j):
        if i < 0 or i >= rows or j < 0 or j >= columns or grid[i][j] != '1':
            return
        
        grid[i][j] = '2'
        
        self.mark_visited(grid, rows, columns, i+1, j)
        self.mark_visited(grid, rows, columns, i-1, j)
        self.mark_visited(grid, rows, columns, i, j+1)
        self.mark_visited(grid, rows, columns, i, j-1)
        
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        islands = 0
        rows = len(grid)
        columns = len(grid[0])
        
        if rows == 0 or columns == 0:
            return
        
        for i in range(rows):
            for j in range(columns):
               if grid[i][j] == '1':
                   islands += 1
                   self.mark_visited(grid, rows, columns, i, j)
                   
        return islands
    
# @lc code=end

