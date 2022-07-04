#
# @lc app=leetcode id=74 lang=python
#
# [74] Search a 2D Matrix
#

# @lc code=start
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # Binary search in a matrix: O(log n)
        if not matrix:
            return
        
        rows = len(matrix)
        row = -1
        array = []
        
        for i in range(rows - 1):
            if matrix[i][0] <= target < matrix[i + 1][0]:
                row = i

        array = matrix[row]

        def binarySearch(left, right):

            if left > right:
                return False
            
            mid = (left + right) // 2
            
            if target == array[mid]:
                return True
            
            elif target < array[mid]:
                return binarySearch(left, mid - 1)
                
            elif target > array[mid]:
                return binarySearch(mid + 1, right)
        
        return binarySearch(0, len(array) - 1)

# @lc code=end

