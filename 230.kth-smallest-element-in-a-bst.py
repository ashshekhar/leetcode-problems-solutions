#
# @lc app=leetcode id=230 lang=python
#
# [230] Kth Smallest Element in a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inOrderTraversal(self, root, result):
        if not root:
            return

        self.inOrderTraversal(root.left, result)
        result.append(root.val)
        self.inOrderTraversal(root.right, result)
        
        return result
            
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        result = []
        
        self.inOrderTraversal(root, result)
        
        return result[k-1]
        
        
# @lc code=end

