#
# @lc app=leetcode id=20 lang=python
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        num = len(s)
        i = num//2 - 1
        j = i+1

        if(num%2 != 0):
            return False

        while i>=0 and j<num:
            if(s[i] == '(' and s[j] == ')' or 
                s[i] == '{' and s[j] == '}' or 
                s[i] == '[' and s[j] == ']'):
                i -= 1
                j += 1
            else:
                return False
        return True

# @lc code=end