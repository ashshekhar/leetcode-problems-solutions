#
# @lc app=leetcode id=145 lang=python
#
# [145] Binary Tree Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # Trivial recursive solution
        # result = []
        
        # def helper(result, root):
        #     if root is None:
        #         return
        #     helper(result, root.left)
        #     helper(result, root.right)
        #     result.append(root.val)
            
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
            
            if current.left:
                stack.append(current.left)
            if current.right:
                stack.append(current.right)
                    
        return result[::-1]
        
# @lc code=end

