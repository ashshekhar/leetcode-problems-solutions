#
# @lc app=leetcode id=342 lang=python
#
# [342] Power of Four
#

# @lc code=start
class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        float(n)

        if(n == 1):
            return True

        if(n%4 != 0):
            return False
        
        while type(n) is int:
            n = float(n/4)
            
            if(n<=0):
                return False
            if(n == 1):
                return True

        return False
# @lc code=end

