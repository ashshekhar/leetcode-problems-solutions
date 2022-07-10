#
# @lc app=leetcode id=85 lang=python
#
# [85] Maximal Rectangle
#

# @lc code=start
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        # O(n) Stack Solution
        # Stores (index, height)
        stack = [(-1, -1)]
        max_area = float("-inf")
        
        for index, height in enumerate(heights):
            
            # Pop on encountering a decreasing height
            # And update max_area
            while stack[-1] != (-1, -1) and height <= stack[-1][1]:
                
                # Finding the area for this number
                old_index, old_height = stack.pop()
                
                # Right limit is new (index, height)
                # Left limit is stack.peek()
                max_area = max(max_area, (index - stack[-1][0] - 1) * old_height)
                
            # Else simply append
            stack.append((index, height))

        # If in the end there are elements left
        while stack[-1] != (-1, -1):

            # Finding the area for this number
            old_index, old_height = stack.pop()

            # Right limit is len(heights) 
            # Left limit is stack.peek()
            max_area = max(max_area, (len(heights) - stack[-1][0] - 1) * old_height)

        return max_area
        
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        # See maximal square too
        # The logic is to find the maximum area of histogram created by each row
        if not matrix:
            return 0
        
        final_res = float("-inf")
        
        dp = [0 for _ in range(len(matrix[0]))]
        
        for i in range(len(matrix)):
            
            # Create Histogram
            for j in range(len(matrix[0])):
                
                # Histogram array per row
                dp[j] = dp[j] + 1 if matrix[i][j] == "1" else 0
            
            # Call max rectangle area per row
            final_res = max(final_res, self.largestRectangleArea(dp))
        
        return final_res
# @lc code=end

