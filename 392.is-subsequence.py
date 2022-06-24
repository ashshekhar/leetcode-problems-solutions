#
# @lc app=leetcode id=392 lang=python
#
# [392] Is Subsequence
#

# @lc code=start
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) == 0 and len(t) > 0:
            return True
        
        i = 0
        j = 0
        
        while i < len(s) and j < len(t):

            if s[i] == t[j]:
                i += 1
                j += 1
                
            else:
                j += 1
        
        if  i - 1 == len(s) - 1:
            return True
        
        return False
# @lc code=end

