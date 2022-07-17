"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        # We create nodes in inorder fashion
        # Also keep track on prev node (varying) and head node (first node)
        if not root:
            return None
        
        global prev
        prev = None
        
        global head
        head = None
        
        def inorder(node):
            global prev, head
            
            if not node:
                return None
            
            # left
            inorder(node.left)
            
            # Node: First node in DLL
            if not prev:
                head = node
                prev = head
                
            else:
                prev.right = node
                node.left = prev
                prev = node
            
            # Right
            inorder(node.right)
    
        inorder(root)
        
        # Complete the circular link
        head.left = prev
        prev.right = head
        
        return head