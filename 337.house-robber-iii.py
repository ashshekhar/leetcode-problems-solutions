#
# @lc app=leetcode id=337 lang=python
#
# [337] House Robber III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def dfs(self, root):
        if not root:
            return [0, 0]
        
        left_pair = self.dfs(root.left)
        right_pair = self.dfs(root.right)
        
        with_root = root.val + left_pair[1] + right_pair[1]
        without_root = max(left_pair) + max(right_pair)
        
        return [with_root, without_root]
        
        
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # DFS Algorithm
        return max(self.dfs(root))
        
# @lc code=end

