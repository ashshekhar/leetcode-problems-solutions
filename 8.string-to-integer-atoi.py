#
# @lc app=leetcode id=8 lang=python
#
# [8] String to Integer (atoi)
#

# @lc code=start
class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Remove leading and trailing whitespace
        s = s.strip()
        
        pos_sign = neg_sign = False
        num = 0
        
        # Empty input
        if not s:
            return 0
        
        # First char should be + or -
        if s[0] == '-':
            neg_sign = True
            
        elif s[0] == '+':
            pos_sign = True
        
        # If first char is not + or - and also not a digit, return 0
        elif not s[0].isdigit():
            return 0
        
        # Else if first char is not + or -, but a numeric
        elif s[0].isdigit():
            num = ord(s[0]) - ord("0")
            pos_sign = True
        
        # Now next allowed characters are only numeric, else break out and return
        for i in range(1, len(s)):
            if s[i].isdigit():
                num = num * 10 + ord(s[i]) - ord("0")
            else:
                break
            
        if pos_sign:
            num = num
            
        elif neg_sign:
            num = -1 * num
        
        # If number greater than 32 bits  
        if num > 2**31 - 1: 
            return 2**31 - 1
        
        elif num < -2**31: 
            return -2**31
        
        return num
# @lc code=end

