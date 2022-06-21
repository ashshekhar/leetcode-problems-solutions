#
# @lc app=leetcode id=54 lang=python
#
# [54] Spiral Matrix
#

# @lc code=start

import numpy as np


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        rows = len(matrix)
        cols = len(matrix[0])
        
        top_left = (0,0)
        top_right = (0, cols - 1)
        bottom_left = (rows - 1, 0)
        bottom_right = (rows - 1, cols  - 1)
        


# @lc code=end
