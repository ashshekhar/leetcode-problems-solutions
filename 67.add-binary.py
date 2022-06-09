#
# @lc app=leetcode id=67 lang=python
#
# [67] Add Binary
#

# @lc code=start
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        i = 0
        j = 0
        
        val_a = 0
        val_b = 0
    
        for str in a[::-1]:
            val_a += int(str) * (2 ** i)
            i += 1
            
        for str in b[::-1]:
            val_b += int(str) * (2 ** j)
            j += 1
    
        return format(val_a + val_b, "b")
     
# @lc code=end

