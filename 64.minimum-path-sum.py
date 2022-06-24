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
        min_sum = grid[0][0]
        
        for i in range(1, cols):
            dp[0][i] = grid[0][i] + dp[0][i-1]
            
            if dp[0][i] < min_sum:
                min_sum = dp[0][i]
        
        for j in range(1, rows):
            dp[j][0] = grid[j][0] + dp[j-1][0]
            
            if dp[j][0] < min_sum:
                min_sum = dp[j][0]
        
        for i in range(1, rows):
            for j in range(1, cols):
                dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
        
        return dp[rows - 1][cols - 1]

# @lc code=end