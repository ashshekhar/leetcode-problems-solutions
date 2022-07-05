#
# @lc app=leetcode id=329 lang=python
#
# [329] Longest Increasing Path in a Matrix
#

# @lc code=start
class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        rows = len(matrix)
        cols = len(matrix[0])
        
        # global res
        # res = 0
        
        final = 0
        
        dp = [[None for _ in range(cols)] for _ in range(rows)]
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        def isValid(row, col, prev_val):
            return not (row < 0 or row >= rows or col < 0 or col >= cols or 
                        prev_val >= matrix[row][col])
        
        # Without Caching - Using an increasing "length" variable and without visited set
        # def dfs(row, col, prev_val, length):

        #     global res
        #     res = max(res, length)
            
        #     for direction in directions:
        #         new_r = row + direction[0]
        #         new_c = col + direction[1]
                
        #         if isValid(new_r, new_c, prev_val):
        #             dfs(new_r, new_c, matrix[new_r][new_c], length + 1)

        #     return res
        
        # With Caching - Using the base result +1 for new result
        def dfs(row, col, prev_val):
            
            if dp[row][col]:
                return dp[row][col]
            
            # The current grid is also counted
            res = 1
            
            for direction in directions:
                new_r = row + direction[0]
                new_c = col + direction[1]
                
                if isValid(new_r, new_c, prev_val):
                    res = max(res, 1 + dfs(new_r, new_c, matrix[new_r][new_c]))
            
            dp[row][col] = res
            return res
        
        for r in range(rows):
            for c in range(cols):
                final = max(final, dfs(r, c, matrix[r][c]))
        
        return final
        
# @lc code=end

