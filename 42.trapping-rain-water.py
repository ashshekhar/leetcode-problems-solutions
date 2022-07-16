#
# @lc app=leetcode id=42 lang=python
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # Trappable water at each index is min(Lmax, Rmax) - height[i] if positive else not possible
        length = len(height)
        left_max = [0] * length
        right_max = [0] * length
        result = 0

        left_max[0] = 0
        right_max[length - 1] = 0
        
        # The left max of each index, is the max of prev left_max and prev_height
        for i in range(1, length):
            left_max[i] = max(left_max[i-1], height[i-1])
        
        # The right max of each index, is the max of next right_max and next_height
        for i in range(length - 2, -1, -1):
            right_max[i] = max(right_max[i+1], height[i+1])
        
        # Find the result
        for i in range(length):
            diff = min(left_max[i], right_max[i]) - height[i]
            if diff > 0:
                result += diff
        
        return result
            
   
# @lc code=end

