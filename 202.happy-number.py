#
# @lc app=leetcode id=202 lang=python
#
# [202] Happy Number
#

# @lc code=start
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        squares = {i: i**2 for i in range(10)}
        
        # To detect repeating cycles and return False
        visited = set()

        summation = 0
        
        while n > 0:
            
            if summation == 1:
                return True
            
            # Cycle
            elif n in visited:
                return False
            
            else:
                summation = 0
                visited.add(n)
                
                while n > 0:
                    dig = n % 10
                    n = n // 10
                    summation += squares[dig]
            
            # Prepare n for the next iteration          
            n = summation
        
    
# @lc code=end

