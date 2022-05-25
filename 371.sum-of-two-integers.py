#
# @lc app=leetcode id=371 lang=python
#
# [371] Sum of Two Integers
#

# @lc code=start

# Code it in Java for correct functioning working

class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        while (b!= 0):
            temp = (a&b) << 1 # Carry
            a = a^b # XOR
            b = temp
        
        return a
        
        
# @lc code=end

