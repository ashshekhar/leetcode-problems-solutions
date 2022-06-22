from collections import deque

class Solution(object):
  def minKnightMoves(self, x, y):
    """
    :type x: int
    :type y: int
    :rtype: int
    """
    def bfs(row, col):
      
      queue = deque()
      visited = set()
      res = 0
      coordinates = [(2, 1), (2, -1), (-2, 1), (-2, -1), (-1, 2), (-1, -2), (1, -2), (1, 2)]
      
      visited.add((row, col))
      queue.append((row, col))
      
      while queue:
        elements = len(queue)
        
        # Finish one level first before moving on the next neighbors
        # Important to keep track of the result / steps
        for _ in range(elements):
            current_coord = queue.popleft()

            if current_coord[0] == x and current_coord[1] == y:
                return res

            for coordinate in coordinates:
                new_x = current_coord[0] + coordinate[0]
                new_y = current_coord[1] + coordinate[1]
                
                if (new_x, new_y) not in visited:
                    visited.add((new_x, new_y))
                    queue.append((new_x, new_y))

        res += 1
                
    return bfs(0, 0)