from collections import deque

# Return the shortest number of steps to take in the grid to reach food
class Solution(object):
    def getFood(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        q = deque()
        visited = set()
        
        def bfs(i, j):
            if i < 0 or i > rows - 1 or j < 0 or j > cols - 1:
                return
            
            visited.add((i, j))
            q.append((i, j, 0))
            
            while q:
                row, col, count = q.popleft()
                
                if grid[row][col] == "#":
                    return count
                
                for direction in directions:
                    new_row, new_col = row + direction[0], col + direction[1]
                    
                    if new_row < 0 or new_row > rows- 1 or new_col < 0 or new_col > cols - 1 or grid[new_row][new_col] == "X":
                        continue
                    
                    if (new_row, new_col) not in visited:
                        visited.add((new_row, new_col))
                        q.append((new_row, new_col, count + 1))
            return -1
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "*":
                    return bfs(i, j)