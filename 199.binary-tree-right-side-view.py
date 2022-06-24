#
# @lc app=leetcode id=199 lang=python
#
# [199] Binary Tree Right Side View
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
        
        if root.right:
            self.helper(root.right, index+1, result)
            
        if root.left:
            self.helper(root.left, index+1, result)
        
        return result
    
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # Create a hashmap with nodes from right to left as values and level as keys

        # Level order traversal
        if not root:
            return
        
        result = []
        index = 0
        final = []
        
        res = self.helper(root, index, result)

        for results in res:
            final.append(results[0])

        return final

# @lc code=end

