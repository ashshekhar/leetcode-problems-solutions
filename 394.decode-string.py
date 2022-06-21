#
# @lc app=leetcode id=394 lang=python3
#
# [394] Decode String
#

# @lc code=start
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []

        if s == "":
            return ""
        
        for char in s:
            if char != "]":
                stack.append(char)
                
            elif char == "]":
                substr = ""
                
                while stack[-1] != "[":
                    substr = stack.pop() + substr
                stack.pop()

                numeric = ""
                while stack and stack[-1].isdigit():
                    numeric = stack.pop() + numeric

                stack.append(int(numeric) * substr)
                
        return ''.join(stack)
        
# @lc code=end

