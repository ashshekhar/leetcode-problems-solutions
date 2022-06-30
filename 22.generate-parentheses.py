#
# @lc app=leetcode id=22 lang=python
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # Classic backtracking problem
        res = []
        stack = []
        
        def backtrack(open_count, closing_count):
            
            if open_count == closing_count == n:
                res.append("".join(stack))
                return
            
            if open_count < n:
                stack.append("(")
                backtrack(open_count + 1, closing_count)
                stack.pop()
                
            if closing_count < open_count:
                stack.append(")")
                backtrack(open_count, closing_count + 1)
                stack.pop()
            
        backtrack(0, 0)
        return res
# @lc code=end

