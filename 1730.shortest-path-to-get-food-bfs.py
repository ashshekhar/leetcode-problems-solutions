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
        
        def validCoordinate(row, col):
            return not(row < 0 or row >= rows or col < 0 or col >= cols or \
                    grid[row][col] == "X" or (row, col) in visited)

        def bfs(i, j):
            count = 0
            visited.add((i, j))
            q.append((i, j))
            
            while q:
                for _ in range(len(q)):
                    row, col = q.popleft()
                    
                    if grid[row][col] == "#":
                        return count
                    
                    for direction in directions:
                        new_row, new_col = row + direction[0], col + direction[1]

                        if validCoordinate(new_row, new_col):
                            visited.add((new_row, new_col))
                            q.append((new_row, new_col))
                    
                count += 1
                            
            return -1
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "*":
                    return bfs(i, j)