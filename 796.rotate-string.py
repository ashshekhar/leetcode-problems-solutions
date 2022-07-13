#
# @lc app=leetcode id=796 lang=python
#
# [796] Rotate String
#

# @lc code=start
class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        for i in range(len(s)):
  
            if s[i: len(s)] + s[ :i] == goal:
                return True
            
        return False
        
# @lc code=end

