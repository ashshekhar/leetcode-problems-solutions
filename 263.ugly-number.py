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
        
        primes = [2, 3, 5]
        
        # An ugly number, if kept being divided by 2, 3 or 5 reduces to 1
        for prime in primes:
            
            while n % prime == 0:
                n = n // prime
                
        return n == 1
            
# @lc code=end

