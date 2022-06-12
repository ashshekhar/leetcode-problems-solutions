#
# @lc app=leetcode id=14 lang=python
#
# [14] Longest Common Prefix
#

# @lc code=start
from collections import deque

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        length = len(strs)
        i = 0

        if length == 0:
            return ""
        
        if length == 1:
            return strs[0]
        
        strs = sorted(strs, key=lambda x: len(x))
        smallest = strs[0]
        
        while len(smallest) > 0:
            for i in range(1, len(strs)):
                if smallest in strs[i][:len(smallest)]:
                    flag = True
                else:
                    flag = False
                    break
                
            if flag:
                return smallest if len(strs) > 0 else ""
            else:  
                smallest = smallest[:len(smallest)-1]
            
        return ""
        
# @lc code=end

