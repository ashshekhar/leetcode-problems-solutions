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
        result = []
        while len(matrix):
            try:
                result += matrix.pop(0)
                result += [i.pop() for i in matrix]
                result += matrix.pop()[::-1]
                result += [i.pop(0) for i in matrix[::-1]]
            except:
                break
        
        return result

# @lc code=end
