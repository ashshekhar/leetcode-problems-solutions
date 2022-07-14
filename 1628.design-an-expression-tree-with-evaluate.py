import abc
from abc import ABCMeta, abstractmethod 
"""
This is the interface for the expression tree Node.
You should not remove it, and you can define some classes to implement it.
"""

class Node:
    __metaclass__ = ABCMeta
    # define your fields here
    @abstractmethod
    def evaluate(self):
        pass

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
    def evaluate(self):
        
        if not self.val:
            return 0
        
        # Leaf node is the int val
        if not self.left and not self.right:
            return self.val
        
        left_ans = self.left.evaluate()
        right_ans = self.right.evaluate()
        
        # The node is the operator val
        if self.val == "+":
            return left_ans + right_ans
                
        if self.val == "-":
            return left_ans - right_ans
                
        if self.val == "*":
            return left_ans * right_ans
                
        if self.val == "/":
            return left_ans // right_ans
        
"""    
This is the TreeBuilder class.
You can treat it as the driver code that takes the postinfix input
and returns the expression tree represnting it as a Node.
"""

class TreeBuilder(object):
    def buildTree(self, postfix):
        """
        :type s: List[str]
        :rtype: int
        """
        stack = []
        
        operations = "+*/-"
        
        for char in postfix:
            
            if char not in operations:
                node = TreeNode(int(char))
                stack.append(node)
                
            else:
                op = TreeNode(char)
                op.right = stack.pop()
                op.left = stack.pop()
                
                stack.append(op)
        
        return stack[-1]
      
"""
Your TreeBuilder object will be instantiated and called as such:
obj = TreeBuilder();
expTree = obj.buildTree(postfix);
ans = expTree.evaluate();
"""
        