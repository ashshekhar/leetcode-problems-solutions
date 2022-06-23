#
# @lc app=leetcode id=224 lang=python
#
# [224] Basic Calculator
#

# @lc code=start
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        sum = 0
        sign = 1 # 1 is positive, -1 is negative
        i = 0
        
        # Input cleaning
        s = s.replace(" ", "")
        s = "(" + s[0:] + ")"

        while i < len(s):
          # Sign
            if s[i] == '-':
                sign = -1
            elif s[i] == '+':
                sign = 1
                
            # Number: Can be multi digit
            if s[i].isdigit():
                num = 0
                
                while s[i].isdigit() and i < len(s):
                    # print(s, i, s[i])
                    num = 10*num + int(s[i])
                    i += 1

                sum += num * sign
                i -= 1
                
            # (
            if s[i] == '(':
                stack.append(sum)
                stack.append(sign)
                sum = 0
                sign = 1
            
            # )
            if s[i] == ')':
                if stack:
                    sum = sum * stack.pop()
                    sum += stack.pop()
                    
            i += 1
            
        return sum
            
# @lc code=end

