#
# @lc app=leetcode id=572 lang=python
#
# [572] Subtree of Another Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def checkSameTree(self, root1, root2):
        if not root1 and not root2:
            return True
        
        elif (root1 and not root2) or (root2 and not root1):
            return False
        
        return root1.val == root2.val and self.checkSameTree(root1.left, root2.left) and self.checkSameTree(root1.right, root2.right)
    
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        if not root or not subRoot:
            return
        
        if self.checkSameTree(root, subRoot):
            return True
        
        if self.isSubtree(root.left, subRoot):
            return True
        
        if self.isSubtree(root.right, subRoot):
            return True

        return False

# @lc code=end

