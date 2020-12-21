#
# @lc app=leetcode id=13 lang=python
#
# [13] Roman to Integer
#

# @lc code=start
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        integer = 0
        i = 0
        roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

        while(i<len(s)):
            if(s[i] == 'I' and i<len(s)-1): 
                if(s[i+1] == 'V'):
                    integer += 4
                    i += 2
                    continue
                if(s[i+1] == 'X'):
                    integer += 9
                    i += 2
                    continue

            elif(s[i] == 'X' and i<len(s)-1): 
                if(s[i+1] == 'L'):
                    integer += 40
                    i += 2
                    continue
                if(s[i+1] == 'C'):
                    integer += 90
                    i += 2
                    continue

            elif(s[i] == 'C' and i<len(s)-1): 
                if(s[i+1] == 'D'):
                    integer += 400
                    i += 2
                    continue
                if(s[i+1] == 'M'):
                    integer += 900
                    i += 2
                    continue

            integer += roman[s[i]]
            i += 1
            
        return integer

# @lc code=end

