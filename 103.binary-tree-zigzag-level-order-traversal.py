#
# @lc app=leetcode id=103 lang=python
#
# [103] Binary Tree Zigzag Level Order Traversal
#

# @lc code=start

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrderTraversal(self, result, root, index):
        
        if not root:
            return
        
        if index < len(result):
            result[index].append(root.val)
        else:
            result.append([root.val])

        if root.left:
            self.levelOrderTraversal(result, root.left, index + 1)
            
        if root.right:
            self.levelOrderTraversal(result, root.right, index + 1)

        return result
        
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        index = 0
        
        res = self.levelOrderTraversal(res, root, index)
        
        if not res:
            return []
        
        for index, traversal in enumerate(res):
            if index % 2 != 0:
                res[index] = traversal[::-1]
        
        return res
      
# @lc code=end
  