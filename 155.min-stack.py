#
# @lc app=leetcode id=155 lang=python
#
# [155] Min Stack
#

# @lc code=start
class MinStack(object):

    def __init__(self):
        self.stack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        # Append (val, min_val till now) in the stack
        if not self.stack:
            self.stack.append([val, val])
        else:
            current_min = min(val, self.stack[-1][1])
            self.stack.append([val, current_min])
    
    def pop(self):
        """
        :rtype: None
        """
        return self.stack.pop()[0]
        
    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        return self.stack[-1][1]
            

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

