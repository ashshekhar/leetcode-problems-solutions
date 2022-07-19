#
# @lc app=leetcode id=304 lang=python
#
# [304] Range Sum Query 2D - Immutable
#

# @lc code=start
class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        rows = len(matrix)
        cols = len(matrix[0])
        
        self.sumMatrix = [[0] * (cols + 1) for _ in range(rows + 1)]
        
        # Calculate and fill the prefix sum such that each square is the bottom left 
        # sum of the biggest square it is a part of
        
        for row in range(rows):
            prefix = 0
            for col in range(cols):
                
                # Taking from the real matrix input
                prefix += matrix[row][col]
                above = self.sumMatrix[row][col + 1]
                
                # Goal is to fill the diagonal right since we added extra row and col
                # prefix is left sum including the number itself, above is top sum
                self.sumMatrix[row + 1][col + 1] = prefix + above
        

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        # Offset the input by 1 since we added extra row and col
        row1, row2, col1, col2 = row1 + 1, row2 + 1, col1 + 1, col2 + 1
         
        bottom_right = self.sumMatrix[row2][col2]
        above = self.sumMatrix[row1 - 1][col2]
        left = self.sumMatrix[row2][col1 - 1]
        top_left = self.sumMatrix[row1 - 1][col1 - 1]
        
        # top_left is subtracted twice - once both in above and left so we add one back
        return bottom_right - above - left + top_left
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
# @lc code=end

