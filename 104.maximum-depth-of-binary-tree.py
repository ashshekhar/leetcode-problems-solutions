#
# @lc app=leetcode id=104 lang=python
#
# [104] Maximum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Recursive approach
        # Each level you go, you add +1 to depth
        # if not root:
        #     return 0
        
        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        # Iterative Approach using Stack
        if not root:
            return 0
        
        stack = [[1, root]]
        depth = 0
        
        while stack:
            current_depth, root = stack.pop()
            depth = max(current_depth, depth)
            
            if root.left:
                stack.append([1 + current_depth, root.left])
            if root.right:
                stack.append([1 + current_depth, root.right])
            
        return depth
        
# @lc code=end

