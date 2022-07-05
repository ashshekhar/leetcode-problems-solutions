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
        # While the carry is not equal to 0, XOR the two numbers and & shift by 1 to find the Carry
        # Now repeat the same on the XOR result and carry shifted by 1
        while (b != 0):
            carry = (a & b) << 1 # Carry
            a = a^b # XOR
            b = carry
        
        return a
        
        
# @lc code=end

