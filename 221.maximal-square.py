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
        
        for i in range(row):
            matrix[i][0] = int(matrix[i][0])
            max_val = max(max_val, matrix[i][0])
            
        for j in range(cols):
            matrix[0][j] = int(matrix[0][j])
            max_val = max(max_val, matrix[0][j])

        for i in range(1, row):
            for j in range(1, cols):
                if matrix[i][j] == "1":
                    matrix[i][j] = 1 + int(min(int(matrix[i-1][j]), int(matrix[i][j-1]), int(matrix[i-1][j-1])))
                    max_val = max(max_val, matrix[i][j])
                
                elif matrix[i][j] == "0":
                    matrix[i][j] = 0

        return max_val ** 2
                    
        
# @lc code=end

