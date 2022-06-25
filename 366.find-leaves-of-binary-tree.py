# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isLeaf(self, node):
        return not node.left and not node.right
    
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return
        
        # Only need once
        stack = []
        final = []
        
        def removeLeaves(root):
            # Need for every new call
            res = []
            
            # Down to the only one root = leaf node base case
            if self.isLeaf(root):
                
                final.append([root.val])
                root.val = -1
                return
            
            stack.append(root)

            while stack:

                current_node = stack.pop()

                if current_node.left and not self.isLeaf(current_node.left):
                    stack.append(current_node.left)

                elif current_node.left and self.isLeaf(current_node.left):
                    res.append(current_node.left.val)
                    current_node.left = None

                if current_node.right and not self.isLeaf(current_node.right):
                    stack.append(current_node.right)

                elif current_node.right and self.isLeaf(current_node.right):
                    res.append(current_node.right.val)
                    current_node.right = None 

            if not stack:
                final.append(res)
        
        while root.val != -1:
            removeLeaves(root)

        return final