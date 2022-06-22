#
# @lc app=leetcode id=73 lang=python
#
# [73] Set Matrix Zeroes
#

# @lc code=start
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        row_zeroes = set()
        col_zeroes = set()
        
        rows, columns = len(matrix), len(matrix[0])
        
        for i in range(rows):
            for j in range(columns):
                if matrix[i][j] == 0:
                    row_zeroes.add(i)
                    col_zeroes.add(j)
           
        for row in row_zeroes:
            for i in range(columns):
                matrix[row][i] = 0
        
        for col in col_zeroes:
            for i in range(rows):
                matrix[i][col] = 0    

# @lc code=end

