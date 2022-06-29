#
# @lc app=leetcode id=662 lang=python
#
# [662] Maximum Width of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
from collections import deque

class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # BFS Level Order Traversal
        queue = deque()
        queue.append((0, root))
        
        res = float("-inf")

        while queue:
            
            length = len(queue)
            left_non_null = float("inf")
            right_non_null = float("-inf")

            # Need this loop to calculate the difference of right_non_null and left_non_null at each level
            for _ in range(length):
                index, node = queue.popleft()

                left_non_null = min(left_non_null, index)
                right_non_null = max(right_non_null, index)
                
                if node.left:
                    queue.append((2 * index + 1, node.left))
                
                if node.right:
                    queue.append((2 * index + 2, node.right))

            res = max(res, right_non_null - left_non_null + 1)
            
        return res
        
        
        
# @lc code=end

