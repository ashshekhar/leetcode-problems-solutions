#
# @lc app=leetcode id=236 lang=python
#
# [236] Lowest Common Ancestor of a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        p_path = []
        q_path = []
        lca = root.val
        
        def printPath(node, target, path, final_path):
            if not node:
                return
            
            path.append(node)
            
            if node.val == target.val:
                final_path.append(path[::])
                return
            
            printPath(node.left, target, path, final_path)
            printPath(node.right, target, path, final_path)
            
            path.pop()

        if not root:
            return
        
        printPath(root, p, [], p_path)
        printPath(root, q, [], q_path)

        while p_path[0] and q_path[0] and p_path[0][0].val == q_path[0][0].val:
            lca = p_path[0].pop(0)
            q_path[0].pop(0)
        
        return lca
        
# @lc code=end

