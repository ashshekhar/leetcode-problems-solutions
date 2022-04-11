#
# @lc app=leetcode id=101 lang=python
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetricNew(self, p, q):
        if not p and not q:
            return True

        if p and not q or q and not p:
            return False
    
        if p.val != q.val:
            return False
        
        if p.val == q.val:    
            return self.isSymmetricNew(p.left, q.right) and self.isSymmetricNew(p.right, q.left)
        

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if (not root) or (root.left and not root.right) or (root.right and not root.left):
            return False

        if not root.left and not root.right:
            return True

        if root.left.val == root.right.val:
            return self.isSymmetricNew(root.left, root.right)

# @lc code=end

