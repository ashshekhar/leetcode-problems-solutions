#
# @lc app=leetcode id=7 lang=python
#
# [7] Reverse Integer
#

# @lc code=start
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        res = 0
        neg = False
        
        if x < 0:
            x *= -1
            neg = True
        
        for i in reversed(str(x)):
            res = res * 10 + int(i)
            
        res = -1 * int(res) if neg else int(res)
                                           
        if res > 2**31 - 1 or res < -1 * 2**31:
            return 0
        
        return res
    
# @lc code=end

