#
# @lc app=leetcode id=449 lang=python
#
# [449] Serialize and Deserialize BST
#
from collections import deque
# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        
        preorder = ""
        queue = deque()
        queue.append(root)
        
        while queue:
            node = queue.popleft()
            
            if not node:
                preorder += "N,"
                continue
                
            else:
                preorder += str(node.val) + ","
                
            queue.append(node.left)
        
            queue.append(node.right)
                
        return preorder


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not root:
            return ""
        
        preorder = ""
        queue = deque()
        queue.append(root)
        
        while queue:
            node = queue.popleft()
            
            if not node:
                preorder += "N,"
                continue
                
            else:
                preorder += str(node.val) + ","
                
            queue.append(node.left)
        
            queue.append(node.right)
                
        return preorder

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
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
# @lc code=end

