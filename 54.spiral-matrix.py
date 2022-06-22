#
# @lc app=leetcode id=54 lang=python
#
# [54] Spiral Matrix
#

# @lc code=start

class Solution(object):
    
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        rows = len(matrix)
        cols = len(matrix[0])
        res = []
        
        top_left = [0,0]
        top_right = [0, cols - 1]
        bottom_left = [rows - 1, 0]
        bottom_right = [rows - 1, cols  - 1]
    
        
        while len(res) < rows * cols:

            if top_left == top_right == bottom_left == bottom_right:
                res.append(matrix[top_left[0]][top_left[1]])
                return res
            
            for i in range(top_left[1], top_right[1]):
                if matrix[top_left[0]][i] != 101:
                    res.append(matrix[top_left[0]][i])
                    matrix[top_left[0]][i] = 101
            
            for i in range(top_right[0], bottom_right[0]):
                if matrix[i][bottom_right[1]] != 101:
                    res.append(matrix[i][top_right[1]])
                    matrix[i][bottom_right[1]] = 101
                    
            for i in range(bottom_right[1], bottom_left[1], -1):
                if matrix[bottom_right[0]][i] != 101:
                    res.append(matrix[bottom_right[0]][i])
                    matrix[bottom_right[0]][i] = 101 
            
            for i in range(bottom_left[0], top_left[0], -1):
                if matrix[i][bottom_left[1]] != 101:
                    res.append(matrix[i][bottom_left[1]])
                    matrix[0][bottom_left[1]] = 101
            
            top_left[0] += 1
            top_left[1] += 1
            
            top_right[0] += 1
            top_right[1] += -1
            
            bottom_left[0] += -1
            bottom_left[1] += 1     
          
            bottom_right[0] += -1
            bottom_right[1] += -1    

        return res

# @lc code=end
