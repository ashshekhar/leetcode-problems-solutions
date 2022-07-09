#
# @lc app=leetcode id=124 lang=python
#
# [124] Binary Tree Maximum Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Different from Path Sum III. 
        # Exactly like Diameter of a Binary Tree
        
        # You're finding the max possible, instead of counting all node sequences that sum up to target
        global max_sum
        max_sum = float("-inf")
         
        # Returns the max_sum without split
        def dfs(node):
            global max_sum
            
            if not node:
                return 0
            
            # Ignore negative sum, better to node include them
            left_subtree_sum = max(dfs(node.left), 0)
            right_subtree_sum = max(dfs(node.right), 0)
            
            # Update max_sum with split
            max_sum = max(max_sum, node.val + left_subtree_sum + right_subtree_sum)
            
            # Return the max_sum possible without split 
            return node.val + max(left_subtree_sum, right_subtree_sum)
        
        dfs(root)
        return max_sum
        
# @lc code=end

