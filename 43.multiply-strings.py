#
# @lc app=leetcode id=43 lang=python
#
# [43] Multiply Strings
#

# @lc code=start
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if "0" in [num1, num2]:
            return "0"
        
        # Max result size
        res = [0] * (len(num1) + len(num2))
        
        # Reverse the nums for the index math to work out
        num1 = num1[::-1]
        num2 = num2[::-1]
        
        # Iterate through and create res
        for i1 in range(len(num1)):
            for i2 in range(len(num2)):
                val = int(num1[i1]) * int(num2[i2])
                
                # Max val can be 81, so 1 and 8 are stored and added to prev values if any

                # Initially store 81
                res[i1 + i2] += val
                # Then find out the carry, 8 and store it in the next
                res[i1 + i2 + 1] += res[i1 + i2] // 10
                # Then remove 8 from 81
                res[i1 + i2] = res[i1 + i2] % 10
        
        # Reverse the result and 
        res = res[::-1]
        
        # Get rid of leading zeroes
        begin = 0 
        while begin < len(res) and res[begin] == 0:
            begin += 1
        
        # Map all the integers to string
        res = map(str, res[begin:])
        return "".join(res)
                    
# @lc code=end

