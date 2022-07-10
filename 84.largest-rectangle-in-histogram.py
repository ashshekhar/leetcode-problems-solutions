#
# @lc app=leetcode id=84 lang=python
#
# [84] Largest Rectangle in Histogram
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
        
        
        
        # O(n^2) Approach TLE:
        # Keep track of max area and consider every consecutive pair once
        
        # length = len(heights)
        # max_area = 0
        
        # for i in range(length):
        #     min_height = float("inf")
            
        #     for j in range(i, length):
        #         min_height = min(min_height, heights[j])
        #         current_area = min_height * (j-i+1)
        #         max_area = max(max_area, current_area)
        
        # return max_area     
        
        
        
# @lc code=end

