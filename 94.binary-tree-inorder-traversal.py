#
# @lc app=leetcode id=94 lang=python
#
# [94] Binary Tree Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # Iterative solution
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
            
        # Trivial recursive solution
        # def inorderTraversal(self, root):
        #     """
        #     :type root: TreeNode
        #     :rtype: List[int]
        #     """
        #     result = []
            
        #     def helper(result, root):
        #         if root == None:
        #             return
                
        #         helper(result, root.left)
        
        #         result.append(root.val)
                
        #         helper(result, root.right)
                
        #     helper(result, root)
            
        #     return result
        
        #Iterative Approach
        result = []
        stack = []
        current = root
        
        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            
            current = stack.pop()
            result.append(current.val)
            current = current.right
            
        return result

# @lc code=end

