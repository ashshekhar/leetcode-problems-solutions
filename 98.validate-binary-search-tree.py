#
# @lc app=leetcode id=98 lang=python
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def valid(self, node, left_bound, right_bound):
        if not node:
            return True
        
        if not (node.val > left_bound and node.val < right_bound):
            return False
        
        return self.valid(node.left, left_bound, node.val) and self.valid(node.right, node.val, right_bound)
    
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return

        return self.valid(root, float("-inf"), float("inf"))
        
# @lc code=end

