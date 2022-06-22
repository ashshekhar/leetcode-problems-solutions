#
# @lc app=leetcode id=50 lang=python
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution(object):
    def helper(self, x, n):
        if n == 0:
            return 1

        elif n == -1:
            return 1/x
        
        if x == 1:
            return x
        
        elif x == 0:
            return 0
        
        result = self.helper(x, n//2)
        result = result * result
        return result if n%2 == 0 else x * result
            
        
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # Better Approach
        # 2^10 = (2^5) * (2^5) and keep breaking it down
        neg = False
        
        if n < 0:
            neg = True
    
        n = abs(n)
        
        res = self.helper(x, n)

        if neg:
            return 1/res
        return res
    
        # Basic Approach: Passes 301/305 test case; TLE in rest
        # neg = False
            
        # if n < 0:
        #     neg = True
            
        # elif n == 1:
        #     return x

        # elif n == 0:
        #     return 1

        # elif n == -1:
        #     return 1/x
        
        # if x == 1:
        #     return x

        # n = abs(n)
        # res = 1
        
        # while n >= 1:
        #     res *= x
        #     n -= 1
            
        #     if res == 0:
        #         return res

        # if neg:
        #     return 1/res
        # return res
    
    
# @lc code=end

