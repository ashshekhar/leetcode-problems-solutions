#
# @lc app=leetcode id=263 lang=python
#
# [263] Ugly Number
#

# @lc code=start
class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 0 or n == 0:
            return False
        
        if n == 1:
            return True
        
        # An ugly number, if kept being divided by 2, 3 and 5 reduces to 1
        while n%2 == 0 or n%3 == 0 or n%5 == 0:
            if n%2 == 0:
                n = n // 2
                
            if n%3 == 0:
                n = n // 3
                
            if n%5 == 0:
                n = n // 5
                
        return n == 1
            
# @lc code=end

