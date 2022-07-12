#
# @lc app=leetcode id=1293 lang=python
#
# [1293] Shortest Path in a Grid with Obstacles Elimination
#

# @lc code=start
from collections import deque

class Solution(object):
    def shortestPath(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])
        target = (rows - 1, cols - 1)

        # If we have sufficient quotas to eliminate the obstacles in the worst case,
        # then the shortest distance is the Manhattan distance
        if k >= rows + cols - 2:
            return rows + cols - 2

        # (row, col, remaining quota to eliminate obstacles)
        state = (0, 0, k)
        
        # (steps, state)
        queue = deque([(0, state)])
        seen = set([state])

        while queue:

            steps, (row, col, k) = queue.popleft()

            # We reach the target here
            if (row, col) == target:
                return steps

            # Explore the four directions in the next step
            for new_row, new_col in [(row, col + 1), (row + 1, col), (row, col - 1), (row - 1, col)]:
                
                # If (new_row, new_col) is within the grid boundaries
                if (0 <= new_row < rows) and (0 <= new_col < cols):
                    
                    new_eliminations_left = k - grid[new_row][new_col]
                    new_state = (new_row, new_col, new_eliminations_left)
                    
                    # Add the next move in the queue if it qualifies
                    if new_eliminations_left >= 0 and new_state not in seen:
                        seen.add(new_state)
                        queue.append((steps + 1, new_state))

        # Did not reach the target
        return -1
        
# @lc code=end

