#
# @lc app=leetcode id=102 lang=python
#
# [102] Binary Tree Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def helper(self, root, index, result):
        
        if index < len(result):
            result[index].append(root.val)
        else:
            result.append([root.val])
        
        if root.left:
            self.helper(root.left, index+1, result)
        if root.right:
            self.helper(root.right, index+1, result)
        
        return result
    
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # BFS uses queue
        if not root:
            return
        
        result = []
        index = 0
        
        return self.helper(root, index, result)
        
# @lc code=end

