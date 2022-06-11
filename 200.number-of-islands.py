#
# @lc app=leetcode id=200 lang=python
#
# [200] Number of Islands
#

# @lc code=start
class Solution(object):
    def mark_neighbors_visited(self, grid, row, column, rows, columns):
        if row < 0 or column < 0 or row > rows - 1 or column > columns - 1 or grid[row][column] != '1':
            return
        
        grid[row][column] = '2'
        
        directions = [[0, -1], [-1, 0], [1, 0], [0, 1]]
        
        for direction in directions:
            self.mark_neighbors_visited(grid, row+direction[0], column+direction[1], rows, columns)
    
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return
        
        rows = len(grid)
        columns = len(grid[0])
        count = 0
        
        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == '1':
                    count += 1
                    self.mark_neighbors_visited(grid, i, j, rows, columns)
        
        return count
# @lc code=end

