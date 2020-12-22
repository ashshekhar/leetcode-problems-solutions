#
# @lc app=leetcode id=20 lang=python
#
# [20] Valid Parentheses
#

# @lc code=start
from collections import deque

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Best DS for such problems are stacks
        num = len(s)
        parentheses = deque()
        brackets = {'(':')', '{':'}', '[':']'}

        if(num%2 != 0):
            return False

        for bracket in s:
            # Append opening brackets
            if bracket in brackets:
                parentheses.append(bracket)

            # Pop if corresponding closing bracket found
            elif len(parentheses)>0 and bracket == brackets[parentheses[-1]]:
                parentheses.pop()

            # No corresponding opening bracket found or unwanted closing parentheses
            else:
                return False

        return not parentheses
# @lc code=end