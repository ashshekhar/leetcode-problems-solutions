#
# @lc app=leetcode id=106 lang=python
#
# [106] Construct Binary Tree from Inorder and Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder or not postorder:
            return None
        
        length = len(inorder)
        
        root = TreeNode(postorder[length - 1])
    
        root_index = inorder.index(postorder[length- 1])
        
        root.left = self.buildTree(inorder[:root_index], postorder[:root_index])
        
        root.right = self.buildTree(inorder[root_index + 1: ], postorder[root_index: length])
        
        return root
        
# @lc code=end

