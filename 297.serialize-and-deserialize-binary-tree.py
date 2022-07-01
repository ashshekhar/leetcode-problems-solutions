#
# @lc app=leetcode id=297 lang=python
#
# [297] Serialize and Deserialize Binary Tree
#

# @lc code=start  
from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        
        levelorder = ""
        queue = deque()
        queue.append(root)
        
        while queue:
            node = queue.popleft()
            
            if not node:
                levelorder += "N,"
                continue
                
            else:
                levelorder += str(node.val) + ","
                
            queue.append(node.left)
        
            queue.append(node.right)
                
        return levelorder

        # "1,2,3,N,N,4,5,N,N,N,N"

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        nodes = data.split(",")

        if not nodes or not nodes[0]:
            return None
        else:
            root = TreeNode(int(nodes[0]))
            
        queue = deque()
        queue.append(root)
        index = 1
        
        while queue and index < len(nodes):
            node = queue.popleft()

            if nodes[index] != "N":
                left = TreeNode(int(nodes[index]))
                node.left = left
                queue.append(left)
                
            index += 1

            if nodes[index] != "N":
                right = TreeNode(int(nodes[index]))
                node.right = right
                queue.append(right)
                
            index += 1
        
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# @lc code=end

