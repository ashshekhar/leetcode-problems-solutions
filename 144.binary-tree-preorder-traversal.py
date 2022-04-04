#
# @lc app=leetcode id=144 lang=python
#
# [144] Binary Tree Preorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # Trivial recursive approach
        # result = []
        # def helper(result, root):
        #     if root is None:
        #         return
        #     result.append(root.val)
        #     helper(result, root.left)
        #     helper(result, root.right)

        # helper(result, root)
        
        # return result
        
        # Iterative Approach
        result = []
        stack = []
        
        if root is None:
            return
        
        current = root
        
        stack.append(root)
        
        while stack:
            current = stack.pop()
            result.append(current.val)
            
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
                    
        return result

# @lc code=end

