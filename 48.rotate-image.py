#
# @lc app=leetcode id=48 lang=python
#
# [48] Rotate Image
#

# @lc code=start
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix[0])
        
        # Set a left and right boundary for rows
        # Set a top and bottom boundary for columns
        left, right = 0, length - 1
        top, bottom = 0, length - 1
        
        # Number of layers to rotate
        while top < bottom:
            
            # Number of rotations in this layer
            for i in range(right - left):
                
                # Write this for outermost corners (without i), 
                # Then use i to generalize based on which out of row, col will change
                temp = matrix[bottom - i][left]
                
                matrix[bottom - i][left] = matrix[bottom][right - i]
                matrix[bottom][right - i] = matrix[top + i][right] 
                matrix[top + i][right] = matrix[top][left  + i]
                
                matrix[top][left + i] = temp
            
            left += 1
            right -= 1
            top += 1
            bottom -= 1
        
# @lc code=end