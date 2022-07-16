#
# @lc app=leetcode id=69 lang=python
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        
        if 1 <= x <= 3:
            return 1
        
        # Searching for the answer within these bounds
        left = 1
        right = x // 2
        
        while left <= right:
            mid = left + (right - left) // 2
            
            sq = mid * mid
            if sq == x:
                return mid
            
            if sq < x:
                left = mid + 1
                
            elif sq > x:
                right = mid - 1
        
        # Here when right < left
        return right
        
# @lc code=end

