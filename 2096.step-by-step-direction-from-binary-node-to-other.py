# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution(object):
    def getDirections(self, root, startValue, destValue):
        """
        :type root: Optional[TreeNode]
        :type startValue: int
        :type destValue: int
        :rtype: str
        """
        
        global res
        res = []
        
        s_path = deque()
        t_path = deque()
        
        def preorder(node, target, path):
            global res
            
            if not node:
                return False

            if node.val == target:
                return True
            
            if preorder(node.left, target, path):
                path.appendleft("L")
                return True
            
            if preorder(node.right, target, path):
                path.appendleft("R")
                return True

        # The idea is that we find paths for both start and target nodes.
        preorder(root, startValue, s_path)  
        preorder(root, destValue, t_path)

        # Once we have found them we reduce paths to a lowest common parent node.
        while s_path and t_path and s_path[0] == t_path[0]:
            s_path.popleft()
            t_path.popleft()
            
        # We change the all items in path of start to 'U' and keep the path of target same.
        return 'U' * len(s_path) + ''.join(t_path)
                