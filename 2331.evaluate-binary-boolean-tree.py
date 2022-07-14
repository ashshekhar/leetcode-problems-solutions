# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def evaluateTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if not root:
            return False
        
        # Boolean values found at leaf
        if not root.left and not root.right:
            return root.val != 0
        
        left_expr = self.evaluateTree(root.left)
        right_expr = self.evaluateTree(root.right)
        
        # Use the booleans received and recurse up
        if root.val == 2:
            return (left_expr or right_expr)
              
        if root.val == 3:
            return (left_expr and right_expr)