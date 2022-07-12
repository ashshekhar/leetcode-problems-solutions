# This is a version of original question 1730
# Instead of counting the number of steps, DFS checks if it is possible to visit the food or not
class Solution(object):
    def getFood(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        
        def dfs(i, j):
            if i > rows - 1 or j > cols - 1 or i < 0 or j < 0 or grid[i][j] == "X" or (i, j) in visited:
                return
            
            elif grid[i][j] == "#":
                return True
            
            directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
            
            for direction in directions:
                visited.add((i, j))
                
                if dfs(i + direction[0], j + direction[1]):
                    return True
            
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "*":
                    if dfs(i, j):
                        return True

        return -1