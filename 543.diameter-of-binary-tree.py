#
# @lc app=leetcode id=543 lang=python
#
# [543] Diameter of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # The idea is to build a relation between height of binary tree and 
        # at any given node and using it to build the diameter
        
        # The diameter at each node is the sum of left_height and right_height
        
        global diameter
        diameter = 0

        # Return height which is (1 + max(left, right)) at each node
        def dfs(node):
            
            # Height at null node
            if not node:
                return 0

            left_subtree_height = dfs(node.left)
            right_subtree_height = dfs(node.right)

            # Track the max diameter so far
            global diameter
            diameter = max(diameter, left_subtree_height + right_subtree_height)
            
            # Height for 'node' to add to diameter for above nodes
            return 1 + max(left_subtree_height, right_subtree_height)

        dfs(root)

        return diameter
# @lc code=end

