#
# @lc app=leetcode id=232 lang=python
#
# [232] Implement Queue using Stacks
#

# @lc code=start
class MyQueue(object):

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        # On detecting elements in stack1, empty all of them in stack2, add, and add back
        if not self.stack1:
            self.stack1.append(x)
            
        else:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

            self.stack1.append(x)
            
            while self.stack2:
                self.stack1.append(self.stack2.pop())

    def pop(self):
        """
        :rtype: int
        """
        if self.stack1:
            return self.stack1.pop()

    def peek(self):
        """
        :rtype: int
        """
        return self.stack1[-1]
        

    def empty(self):
        """
        :rtype: bool
        """
        if not self.stack1:
            return True
        return False
        
# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end

