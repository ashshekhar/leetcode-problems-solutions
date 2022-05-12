#
# @lc app=leetcode id=1047 lang=python
#
# [1047] Remove All Adjacent Duplicates In String
#

# @lc code=start
class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Stack solution is the simplest in this case
        stack = []
        
        for i in range(len(s)):
            if stack == []:
                stack.append(s[i])
            
            elif s[i] == stack[-1]:
                stack.pop()
                
            else:
                stack.append(s[i])
              
        return ''.join(stack)  
                
# @lc code=end

