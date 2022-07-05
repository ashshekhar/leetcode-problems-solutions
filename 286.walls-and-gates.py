from collections import deque

class Solution(object):
    def isValid(self, new_r, new_c, rooms, visited, rows, cols):
        if not (new_r < 0 or new_r >= rows or new_c < 0 or new_c >= cols):
            return ((new_r, new_c) not in visited and rooms[new_r][new_c] != -1)
        
        return False
    
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: None Do not return anything, modify rooms in-place instead.
        """
        # Case of Multi-Source BFS
        rows = len(rooms)
        cols = len(rooms[0])
        
        visited = set()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        queue = deque()
        
        # Add the gates to queue
        for i in range(rows):
            for j in range(cols):
                if rooms[i][j] == 0:
                    queue.append((i, j))
                    visited.add((i, j))
        
        depth = 0
            
        # Run multi-source BFS
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                print(r, c)
                rooms[r][c] = depth
                
                for direction in directions:
                    new_r = r + direction[0]
                    new_c = c + direction[1]
                    
                    if self.isValid(new_r, new_c, rooms, visited, rows, cols):
                        visited.add((new_r, new_c))
                        queue.append((new_r, new_c))
                        
            depth += 1