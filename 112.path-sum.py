#
# @lc app=leetcode id=112 lang=python
#
# [112] Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        # Inorder DFS traversal: lnr
        if not root:
            return False
        
        def dfs(node, difference):
            if not node:
                return
                        
            difference -= node.val
            
            # Reached a leaf node, check now
            if not node.left and not node.right:
                return difference == 0

            return dfs(node.left, difference) or dfs(node.right, difference)
        
        return dfs(root, targetSum)
# @lc code=end

