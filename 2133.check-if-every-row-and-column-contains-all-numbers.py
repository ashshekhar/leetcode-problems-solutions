#
# @lc app=leetcode id=2133 lang=python
#
# [2133] Check if Every Row and Column Contains All Numbers
#

# @lc code=start
class Solution(object):
    def checkValid(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        rows = len(matrix)
        cols = len(matrix[0])
        list = []
        
        nums = set()
        
        # Prepare set to check against
        for i in range(1, rows+1):
            nums.add(i)
            
        for row in range(rows):
            # Row Check
            if len(set(matrix[row])) != len(nums):
                return False
            
            # Column Check
            for col in range(cols):
                list.append(matrix[col][row])
            
            if len(set(list)) != len(nums):
                return False
            
            list = []
            
        return True
# @lc code=end

