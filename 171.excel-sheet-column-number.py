#
# @lc app=leetcode id=171 lang=python
#
# [171] Excel Sheet Column Number
#

# @lc code=start
import string
import sys

class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
    
        value = 0
        str_list = list(reversed(columnTitle))
        
        for i in range(len(str_list)):
            value += (ord(str_list[i]) - 64) * (26**i)
        
        return value
# @lc code=end

