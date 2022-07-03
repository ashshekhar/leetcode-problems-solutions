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
            
            # Keep appending till ]
            if char != "]":
                stack.append(char)
            
            # Once encountered, then the strings till "]" are substr
            elif char == "]":
                substr = ""
                
                # Find substr
                while stack[-1] != "[":
                    substr = stack.pop() + substr
                stack.pop()

                # After "]" the values while numeric are the multiplicative factor 
                numeric = ""
                while stack and stack[-1].isdigit():
                    numeric = stack.pop() + numeric

                # Add back the resultant for next iteration
                stack.append(int(numeric) * substr)
                
        return ''.join(stack)
        
# @lc code=end

