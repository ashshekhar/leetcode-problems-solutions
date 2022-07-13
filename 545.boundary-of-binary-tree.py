# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def boundaryOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        right = []
        
        def isLeaf(node):
            return not node.left and not node.right
        
        # Keep going left, unti you can else, right and only add leaf nodes
        def addLeftBoundary(node, res):
            if not node:
                return
            
            while node:
                if not isLeaf(node):
                    res.append(node.val)
                    
                if node.left: node = node.left
                elif node.right: node = node.right
                else: return
            
        # Keep going right, unti you can else, left and only add leaf nodes
        def addRightBoundary(node, right):
            if not node:
                return
            
            while node:
                if not isLeaf(node):
                    right.append(node.val)
                    
                if node.right: node = node.right
                elif node.left: node = node.left
                else: return
                    
        
        # Preorder Traversal
        def addLeaves(node, res):
            if not node:
                return
            
            if isLeaf(node):
                res.append(node.val)
            
            addLeaves(node.left, res)
            addLeaves(node.right, res)
        
        # Main code
        if not root:
            return
        
        if not isLeaf(root):
                res.append(root.val)
        
        addLeftBoundary(root.left, res)
        addLeaves(root, res)
        addRightBoundary(root.right, right)
        
        # Add right traversal in reverse
        for nodes in right[::-1]:
            res.append(nodes)

        return res