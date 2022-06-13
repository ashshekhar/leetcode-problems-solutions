#
# @lc app=leetcode id=844 lang=python
#
# [844] Backspace String Compare
#

# @lc code=start
class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        stack_s = []
        stack_t = []
        
        for char in s:
            if char == '#' and stack_s:
                stack_s.pop()
            else:
                if char != "#":
                    stack_s.append(char)
                
        for char in t:
            if char == '#' and stack_t:
                stack_t.pop()
            else:
                if char != "#":
                    stack_t.append(char)
        
        return stack_s == stack_t
# @lc code=end

