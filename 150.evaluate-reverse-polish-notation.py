#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        
        for token in tokens:
            
            if token in "*+-/":
                second = stack.pop()
                first = stack.pop()
                
                if token == "+":
                    stack.append(first + second)
                    
                elif token == "-":
                    stack.append(first - second)
                    
                elif token == "*":
                    stack.append(first * second)
                    
                elif token == "/":
                    stack.append(int(first / second))
                    
            else:
                stack.append(int(token))

        return stack[-1]
                            
# @lc code=end

