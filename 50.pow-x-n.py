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
        if(n == 1):
            return x

        elif (n == 0):
            return 1

        # Try recursive solution
        output = x * myPow(x, n-1)

        if(n<0):
            return 1/output
        return output
            
# @lc code=end

