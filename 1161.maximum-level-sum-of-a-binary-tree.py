#
# @lc app=leetcode id=1161 lang=python
#
# [1161] Maximum Level Sum of a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return None
        
        traversal = []
        summation = {}
        
        # Level order traversal
        def levelOrderTraversal(node, index, traversal):
            if not node:
                return
            
            if index < len(traversal):
                traversal[index].append((node.val))
            else:
                traversal.append([node.val])
                
            summation[index] = node.val + summation.get(index, 0)
            levelOrderTraversal(node.left, index + 1, traversal)
            levelOrderTraversal(node.right, index + 1, traversal)

        levelOrderTraversal(root, 0, traversal)
        return 1 + max(summation, key = lambda x : summation[x])
# @lc code=end

