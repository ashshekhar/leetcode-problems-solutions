#
# @lc app=leetcode id=538 lang=python
#
# [538] Convert BST to Greater Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # Reverse inorder
        # Go to right, then left then node
        if not root:
            return
        
        global sum
        sum = 0
        
        def dfs(node):
            global sum
            
            if not node:
                return
            
            dfs(node.right)
            
            sum += node.val
            node.val = sum
            
            dfs(node.left)
            
        dfs(root)
        return root
        
# @lc code=end

