#
# @lc app=leetcode id=542 lang=python
#
# [542] 01 Matrix
#

# @lc code=start
class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        rows = len(mat)
        cols = len(mat[0])
        
        # Top left update
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] != 0:
                    left = mat[i][j-1] if j > 0 else float("inf")
                    top = mat[i-1][j] if i > 0 else float("inf")
                    mat[i][j] = 1 + min(top, left)
        
        # Bottom right update
        for i in reversed(range(rows)):
            for j in reversed(range(cols)):
                if mat[i][j] != 0:
                    bottom = mat[i+1][j] if i < rows-1 else float("inf")
                    right = mat[i][j+1] if j < cols-1 else float("inf")
                    mat[i][j] = min(mat[i][j], 1 + min(bottom, right))
                    
        return mat

# @lc code=end

