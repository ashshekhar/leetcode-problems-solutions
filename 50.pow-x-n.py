#
# @lc app=leetcode id=50 lang=python
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        output = 1

        if(n == 1):
            return x

        elif (n == 0):
            return 1

        elif(n > 0):
            for i in range(n):
                output *= x
            return output
            
        elif(n < 0):
            for i in range(-n):
                output *= x
            output = 1/output
            return output         
        
# @lc code=end

