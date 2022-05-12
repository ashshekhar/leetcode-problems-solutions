#
# @lc app=leetcode id=231 lang=python
#
# [231] Power of Two
#

# @lc code=start
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 2 and n != 1:
            return False
        
        if n == 1:
            return True
        
        while n % 2 == 0:
            n = n / 2
        
        return n == 1       
# @lc code=end

