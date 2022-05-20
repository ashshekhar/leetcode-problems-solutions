#
# @lc app=leetcode id=116 lang=python
#
# [116] Populating Next Right Pointers in Each Node
#

# @lc code=start
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def levelOrderTraversal(self, root, index, result):
        if index < len(result):
            result[index].append(root)
        else:
            result.append([root])
        
        if root.left:
            self.levelOrderTraversal(root.left, index + 1, result)
            
        if root.right:
            self.levelOrderTraversal(root.right, index + 1, result)
         
        return result
    
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return root
        
        result = []
        index = 0
        
        traversal = self.levelOrderTraversal(root, index, result)
        
        for level_nodes in traversal:
            if len(level_nodes) == 1:
                continue
            else:
                for i in range(len(level_nodes)-1):
                    level_nodes[i].next = level_nodes[i+1]
        
        return root
                
        
        
        
        
        
# @lc code=end

