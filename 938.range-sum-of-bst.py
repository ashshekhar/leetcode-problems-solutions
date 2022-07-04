#
# @lc app=leetcode id=938 lang=python
#
# [938] Range Sum of BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preOrder(self, node, low, high):

        global res

        if not node:
            return
        
        if low <= node.val <= high:
            res += node.val

        self.preOrder(node.left, low, high)
        
        self.preOrder(node.right, low, high)
        
        return res
    
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        if not root:
            return 0
        
        global res
        res = 0
        
        return self.preOrder(root, low, high)
        
# @lc code=end

