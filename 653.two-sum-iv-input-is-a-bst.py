#
# @lc app=leetcode id=653 lang=python
#
# [653] Two Sum IV - Input is a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if not root:
            return
        
        global res
        res = []
        
        dictionary = {}
        
        def inOrder(node):
            global res
            
            if not node:
                return
            
            inOrder(node.left)
            res.append(node.val)
            inOrder(node.right)
        
        inOrder(root)

        for index, vals in enumerate(res):
            if k - vals not in dictionary:
                dictionary[vals] = index
            else:
                return True
        
        return False
        
# @lc code=end

