#
# @lc app=leetcode id=221 lang=python
#
# [221] Maximal Square
#

# @lc code=start
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        row = len(matrix)
        cols = len(matrix[0])
        
        if row == 1 and cols == 1:
            return int(matrix[0][0])
        
        max_val = 0
        
        # Stores the max length of square with coordinates (r, c) as the top left corner
        dp = {}
        
        def dfs(r, c):
            
            if r >= row or c >= cols or r < 0  or c < 0 or matrix[r][c] == 0:
                return 0
            
            if (r, c) in dp:
                return dp[(r, c)]
            
            right = dfs(r, c + 1)
            down = dfs(r + 1, c)
            diag = dfs(r + 1, c + 1)
            
            if matrix[r][c] == "0":
                dp[(r, c)] = 0
            
            # If "1" then must update the length
            if matrix[r][c] == "1":
                dp[(r, c)] = 1 + min(right, down, diag)
            
            return dp[(r, c)]
        
        dfs(0, 0)
        
        max_val = max(dp.values())
        return max_val ** 2
                    
# @lc code=end

