#
# @lc app=leetcode id=114 lang=python
#
# [114] Flatten Binary Tree to Linked List
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        # dfs returns the last node of the flattened tree
        def dfs(node):
            
            if not node:
                return None
            
            # Only the root node
            if not node.left and not node.right:
                return node
            
            # The tail node of the flattened out left subtree
            left_tail = dfs(node.left)
            
            # The tail node of the fully formed tree rooted at node
            right_tail = dfs(node.right)
            
            # Only case where we need to merge the flattened left side with the flattened right side
            if left_tail:
                left_tail.right = node.right
                node.right = node.left
                node.left = None
            
            # This is not the final return value - Only the return for the next recursion
            # This would be the right_tail node (to attach to node's right) 
            # But if null, then left_tail node
            return right_tail or left_tail
        
        # Not asked to return anything
        dfs(root)
        
# @lc code=end

