#
# @lc app=leetcode id=190 lang=python
#
# [190] Reverse Bits
#

# @lc code=start
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        res = 0
        
        # Since 32 bits
        for _ in range(32):
            res = res << 1
            
            # If even, last digit = bit = 0, else 1
            # bit = n % 2
            bit = n & 1
            
            res += bit
            
            n = n >> 1
        
        return res
               
# @lc code=end

