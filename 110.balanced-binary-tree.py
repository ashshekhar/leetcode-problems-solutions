#
# @lc app=leetcode id=110 lang=python
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    # This method returns the height of a node given
    def getHeight(self, root):
        
        if not root:
            return 0
        
        return 1 + max(self.getHeight(root.left), self.getHeight(root.right))
            
    # This main function checks that each subtree is balanced
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:    
            return True

        left_height = 1 + self.getHeight(root.left)
        right_height = 1 + self.getHeight(root.right)
        
        if abs(left_height - right_height) > 1:
            return False
        
        return self.isBalanced(root.left) and self.isBalanced(root.right)
            
        
# @lc code=end

