#
# @lc app=leetcode id=687 lang=python
#
# [687] Longest Univalue Path
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        global res
        res = 0
        
        if not root:
            return res
        
        if not root.left and not root.right:
            return res
        
        def dfs(node):
            global res
            
            if not node:
                return 0 
            
            left_equal_count = dfs(node.left)
            
            # Increase counts on call back up, if the condition is met, else reset
            if node.left and node.left.val == node.val:
                left_equal_count += 1
            else:
                left_equal_count = 0

            right_equal_count = dfs(node.right)
            
            # Increase counts on call back up, if the condition is met, else reset
            if node.right and node.right.val == node.val:
                right_equal_count += 1
            else:
                right_equal_count = 0

            res = max(res, left_equal_count + right_equal_count)
            
            return max(left_equal_count, right_equal_count)

        dfs(root)
        return res
# @lc code=end

