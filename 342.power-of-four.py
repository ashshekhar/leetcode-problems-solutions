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
        if n < 4 and n != 1:
            return False
        
        if n == 1:
            return True
        
        while n % 4 == 0:
            n = n / 4
        
        return n == 1
# @lc code=end

