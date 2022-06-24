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
        
        def dfs(node, current_sum):
            if not node:
                return
                        
            current_sum += node.val
            
            if not node.left and not node.right:
                return current_sum == targetSum

            return dfs(node.left, current_sum) or dfs(node.right, current_sum)
        
        return dfs(root, 0)
# @lc code=end

