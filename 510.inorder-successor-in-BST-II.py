"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution(object):
    def inorderSuccessor(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        # For a node with right child : l n r follows
        # To find the smallest greater value than node: Go one right and 
        # then left until you can't to get the successor which will give you smallest greater
        current = node
    
        if current.right:
            
            current = current.right
            
            while current.left:
                current = current.left
            return current
        
        # For a node with no immediate right child such as node 2 in example 2
        # a node greater than this would be one of the parents for which this node is either
        # left part or right part. 
        
        # In both cases you keep going up until you reach a value bigger than this node
        else:
            
            # Using BST property
            while current.parent and current.parent.val < node.val:
                current = current.parent
                
            return current.parent
            