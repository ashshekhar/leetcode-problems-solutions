#
# @lc app=leetcode id=257 lang=python
#
# [257] Binary Tree Paths
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        global ans
        ans = []
        
        def preorder(node, path):

            global ans
            
            if not node:
                return
            
            if not node.left and not node.right:
                path.append(str(node.val))
                ans.append(path[::])
                
            else:
                path.append(str(node.val))
            
            preorder(node.left, path)

            preorder(node.right, path)
            
            path.pop()
            
        path = []
        preorder(root, path)
        
        for i in range(len(ans)):
            ans[i] = "->".join(ans[i])
            
        return ans
# @lc code=end

