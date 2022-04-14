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
        row_zeroes = []
        col_zeroes = []
        
        rows, columns = len(matrix), len(matrix[0])
        
        for i in range(rows):
            for j in range(columns):
                if matrix[i][j] == 0:
                    row_zeroes.append(i)
                    col_zeroes.append(j)
                    
        row_zeroes = list(set(row_zeroes))
        col_zeroes = list(set(col_zeroes))
           
        for index in row_zeroes:
            for i in range(columns):
                matrix[index][i] = 0
        
        for index in col_zeroes:
            for i in range(rows):
                matrix[i][index] = 0    

# @lc code=end

