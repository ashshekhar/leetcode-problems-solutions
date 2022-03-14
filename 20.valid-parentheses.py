#
# @lc app=leetcode id=20 lang=python
#
# [20] Valid Parentheses
#

# @lc code=start

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Best DS for such problems are stacks
        # s = "()[]{}"
        
        num = len(s)
        parentheses = []
        
        brackets = {'(':')', '{':'}', '[':']'}

        if(num%2 != 0):
            return False

        for left_bracket in s:
            # Append opening brackets
            if left_bracket in brackets:
                parentheses.append(left_bracket)

            # If parantheses is empty or the right bracket doesn't match the left
            elif len(parentheses) == 0 or brackets[parentheses.pop()] != left_bracket:
                return False
            
        return len(parentheses) == 0
# @lc code=end