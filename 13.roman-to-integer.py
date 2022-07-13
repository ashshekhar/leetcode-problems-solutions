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
        res = 0
        i = 0
        roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

        while i < len(s):
            
            if (i + 1) < len(s) and roman[s[i]] < roman[s[i + 1]]:
                res -= roman[s[i]]
                res += roman[s[i + 1]]
                i += 2
                
            else:
                res += roman[s[i]]
                i += 1
            
        return res

# @lc code=end

