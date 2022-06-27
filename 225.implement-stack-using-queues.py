#
# @lc app=leetcode id=225 lang=python
#
# [225] Implement Stack using Queues
#

# @lc code=start
from collections import deque

class MyStack(object):

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if not self.q1:
            self.q1.append(x)
            
        else:
            while self.q1:
                self.q2.append(self.q1.popleft())

            self.q1.append(x)
            
            while self.q2:
                self.q1.append(self.q2.popleft())
        

    def pop(self):
        """
        :rtype: int
        """
        if self.q1:
            return self.q1.popleft()

    def top(self):
        """
        :rtype: int
        """
        return self.q1[0]
        

    def empty(self):
        """
        :rtype: bool
        """
        if not self.q1:
            return True
        return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# @lc code=end

