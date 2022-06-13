#
# @lc app=leetcode id=191 lang=python
#
# [191] Number of 1 Bits
#

# @lc code=start
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        
        # Bit count
        # for bits in bin(n):
        #     print(bits)
        #     if bits == b'1':
        #         res += 1
        
        # Bit manipulation
        while n!= 0:
            res += 1 if n&1 else 0
            n = n >> 1
        return res
# @lc code=end

