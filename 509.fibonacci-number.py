#
# @lc app=leetcode id=509 lang=python
#
# [509] Fibonacci Number
#

# @lc code=start
class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """ 
        a = 0
        b = 1
        
        if n == 0:
            return a
        
        elif n == 1:
            return b

        for _ in range(2, n  + 1):
            a, b = b, a + b
        
        return b
            
            
#         Recursion
#         global res
#         res = 0
        
#         res = self.helper(n)
        
#         return res
        
    
#     def helper(self, n):

#         global res
        
#         if n == 0:
#             return 0
#         elif n == 1:
#             return 1
        
#         res = self.helper(n - 1)  + self.helper(n - 2)
        
#         return res
    
# @lc code=end

