# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return
        
        queue = deque()
        res = dict()
        
        # BFS Approach
        queue.append([root, 0])
        
        while queue:
            node, index = queue.popleft()
            
            if index not in res:
                res[index] = list()
            
            res[index].append(node.val)
            
            if node.left:
                queue.append([node.left, index - 1])
            
            if node.right:
                queue.append([node.right, index + 1])


        return [res[x] for x in sorted(res.keys())]