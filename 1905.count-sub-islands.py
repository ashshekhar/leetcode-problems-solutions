#
# @lc app=leetcode id=1905 lang=python
#
# [1905] Count Sub Islands
#

# @lc code=start
class Solution(object):
    
    def check_corresponding_island(self, grid1, grid2, row, column, rows, columns, flag):
        if row < 0 or column < 0 or row > rows - 1 or column > columns - 1 or grid2[row][column] == 0 or grid2[row][column] == 2:
            flag = True
            return flag
        
        # Only toggel flag as False when you are sure that there is a 1 in grid2 and corresponding 0 in grid1
        if grid1[row][column] == 0:
            flag = False
        
        # Mark grid2 cell as visited
        grid2[row][column] = 2
    
        directions = [[0, -1], [-1, 0], [1, 0], [0, 1]]
        
        for direction in directions:
            flag = self.check_corresponding_island(grid1, grid2, row+direction[0], column+direction[1], rows, columns, flag) and flag
            
        return flag
    
    def countSubIslands(self, grid1, grid2):
        """
        :type grid1: List[List[int]]
        :type grid2: List[List[int]]
        :rtype: int
        """
        rows = len(grid1)
        columns = len(grid1[0])
        count = 0
        flag = True

        for i in range(rows):
            for j in range(columns):
                if grid2[i][j] == 1:
                    
                    value = self.check_corresponding_island(grid1, grid2, i, j, rows, columns, flag)

                    count += 1 if value else 0
                        
        return count

# @lc code=end

