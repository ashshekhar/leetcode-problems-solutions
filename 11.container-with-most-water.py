#
# @lc app=leetcode id=11 lang=python
#
# [11] Container With Most Water
#

# @lc code=start
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        length = len(height)
        
        if length == 1:
            return 0
        
        max_vol = 0
        current_vol = 0
        
        left_ptr = 0
        right_ptr = length - 1
        
        # Greedy approach: Start with the two end indices
        # Only compromise on the length being shortened by moving either pointers if the height is getting bigger
        # Since that may mean the reduction of volume due to length is offset and exceeded by increment due to height
        
        while left_ptr < right_ptr:
            max_vol = max(max_vol, (right_ptr - left_ptr) * min(height[left_ptr], height[right_ptr]))

            if height[left_ptr] < height[right_ptr]:
                left_ptr += 1
            else:
                right_ptr -= 1
        
        return max_vol
    
        # Brute force approach which exceeds time limit
        # Redundant calculations of volume
        
        # for i in range(length):
        #     j = j = length - 1
            
        #     while i < j and j < length:
        #         current_vol = (j - i) * min(height[i], height[j])
                
        #         if current_vol > max_vol:
        #             max_vol = current_vol

        #         j -= 1
        
        # return max_vol

# @lc code=end

