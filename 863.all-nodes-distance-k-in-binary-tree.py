#
# @lc app=leetcode id=863 lang=python
#
# [863] All Nodes Distance K in Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution(object):
    def distanceK(self, root, target, k):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """
        if not root:
            return
        
        parents = {}
        
        queue = deque()
        visited = set()

        res = []
        
        def create_parents_dictionary(root):
            if not root:
                return
            
            if root.left:
                parents[root.left] = root
                
            if root.right:
                parents[root.right] = root
            
            create_parents_dictionary(root.left)
            create_parents_dictionary(root.right)


        def bfs(res, level, root):
            queue.append((level, root))
            visited.add(root.val)
            
            while queue:
                level, node = queue.popleft()
                
                # Create 2D array of nodes at each level
                if level < k + 1:
                    if level < len(res):
                        res[level].append(node.val)
                    else:
                        res.append([node.val])

                neighbors = []
                if node.left:
                    neighbors.append(node.left)
                if node.right:
                    neighbors.append(node.right)
                if node in parents:
                    neighbors.append(parents[node])

                for neighbor in neighbors:
                    if neighbor.val not in visited:
                        queue.append((level + 1, neighbor))
                        visited.add(neighbor.val)
            
            # If res didn't cover the required steps because of non-availability
            if k + 1 != len(res):
                return []
            else:
                return res[k]
            
        # Create parent dictionary
        create_parents_dictionary(root)

        # Main call
        return bfs(res, 0, target)
# @lc code=end

