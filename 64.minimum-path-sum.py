#
# @lc app=leetcode id=64 lang=python
#
# [64] Minimum Path Sum
#

# @lc code=start
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # Simple dynamic programming problem
        rows = len(grid)
        cols = len(grid[0])
        
        dp = [[0 for _ in range(cols)] for _ in range(rows)] 
        
        # Base case
        dp[0][0] = grid[0][0]

        # First row is shortest to traverse by moving right
        for i in range(1, cols):
            dp[0][i] = grid[0][i] + dp[0][i-1]

        # First column is shortest to traverse by moving down
        for j in range(1, rows):
            dp[j][0] = grid[j][0] + dp[j-1][0]

        # Fill in the rest of the squares except first row and first column
        for i in range(1, rows):
            for j in range(1, cols):
                dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
        
        return dp[rows - 1][cols - 1]

# @lc code=end