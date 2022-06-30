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
        # Go one right and then left unti you can't to get the successor
        
        current = node
        
        if current.right:
            current = current.right
            
            while current.left:
                current = current.left
            return current
        
        # For a node with no right child - the node is some upper node's right part
        # So go up the parent of this node (for which this node is right part) until you can
        # Your answer would be the parent node for which the "top of this chain" is a left child
        else:
            
            # Using BST property
            while current.parent and current.parent.val < node.val:
                current = current.parent
                
            return current.parent
            