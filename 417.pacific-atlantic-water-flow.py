#
# @lc app=leetcode id=417 lang=python
#
# [417] Pacific Atlantic Water Flow
#

# @lc code=start
class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        # We are trying to add to the respective set, all the coordinates that can be achieved from the border cells
        # In other words, can be achieved from the oceans
        
        pacific_visit = set()
        atlantic_visit = set()
        
        rows = len(heights)
        cols = len(heights[0])
        
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        def dfs(row, col, visited, prev_height):
            if (row, col) in visited:
                return
            
            if row < 0 or row >= rows or col < 0 or col >= cols or heights[row][col] < prev_height:
                return
        
            visited.add((row, col))
            
            for direction in directions:
                dfs(row + direction[0], col + direction[1], visited, heights[row][col])

        # Call DFS for each border grids
        for i in range(rows):
            dfs(i, 0, pacific_visit, heights[i][0])
            dfs(i, cols - 1, atlantic_visit, heights[i][cols - 1])
              
        for j in range(cols):
            dfs(0, j, pacific_visit, heights[0][j])
            dfs(rows - 1, j, atlantic_visit, heights[rows - 1][j])
        
        return list(pacific_visit.intersection(atlantic_visit))

# @lc code=end

