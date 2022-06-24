#
# @lc app=leetcode id=113 lang=python
#
# [113] Path Sum II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """
        # The approach is same as Path Sum I with backtracking
        # Backtracking is popping or resetting after all the work needed from a node is done
        if not root:
            return []
    
        current_path = []
        result = []
        
        def dfs(node, current_sum, result, current_path):
            if not node:
                return
            
            current_sum += node.val
            current_path.append(node.val)
        
            if not node.left and not node.right and current_sum == targetSum:
                result.append(list(current_path))
                
            dfs(node.left, current_sum, result, current_path) or dfs(node.right, current_sum, result, current_path)
            
            # Backtracking
            current_path.pop()
        
        dfs(root, 0, result, current_path)
        return result
# @lc code=end

