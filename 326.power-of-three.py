#
# @lc app=leetcode id=326 lang=python
#
# [326] Power of Three
#

# @lc code=start
import sys

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 3 and n != 1:
            return False
        
        if n == 1:
            return True
        
        while n % 3 == 0:
            n = n / 3
        
        return n == 1        
# @lc code=end

