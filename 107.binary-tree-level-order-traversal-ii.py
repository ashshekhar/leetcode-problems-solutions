#
# @lc app=leetcode id=107 lang=python
#
# [107] Binary Tree Level Order Traversal II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def traversal(self, root, result, index):
        
        if index < len(result):
            result[index].append(root.val)
        else:
            result.append([root.val])
        
        if root.left:
            self.traversal(root.left, result, index + 1)
        
        if root.right:
            self.traversal(root.right, result, index + 1)           
        
        return result 
        
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        result = []
        index = 0
        
        rev_result = self.traversal(root, result, index)
        return rev_result[::-1]

# @lc code=end

