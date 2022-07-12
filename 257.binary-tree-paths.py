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
        ans = []         
        
        def dfs(root,s):
            
            if not root:
                return
            
            if not root.left and not root.right:
                ans.append(s + str(root.val))
                return
            
            # Node
            s += str(root.val) 

            # Left
            dfs(root.left,s+"->")
            
            # Right
            dfs(root.right,s+"->")
            
            return
			
            
        dfs(root,"")
        
        return ans
# @lc code=end

