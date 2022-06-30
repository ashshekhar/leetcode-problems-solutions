# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
     
    # Using the BST property
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return
        
        res = None
        
        while root:
            
            # p present in right half
            # Having equal to condition is important, because if we include in else, then p will be returned
            if p.val >= root.val:
                root = root.right
                
            # p present in left half
            else:
                # Possible successor
                res = root
                root = root.left
                
        return res
                
        
      # Trivial: Simply return the next value of out of the inorder traversal
#     def inOrderTraversal(self, node, res):
#         if not node:
#             return
        
#         self.inOrderTraversal(node.left, res)
#         res.append(node)
#         self.inOrderTraversal(node.right, res)
        
#         return res
        
        
#     def inorderSuccessor(self, root, p):
#         """
#         :type root: TreeNode
#         :type p: TreeNode
#         :rtype: TreeNode
#         """
#         res = []
#         final = None
        
#         res = self.inOrderTraversal(root, res)
        
#         for index, nodes in enumerate(res):
            
#             if nodes.val == p.val and index + 1 < len(res):
#                 final = res[index + 1]
#                 break
            
#         return final
        