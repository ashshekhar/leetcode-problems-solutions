#
# @lc app=leetcode id=437 lang=python
#
# [437] Path Sum III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: int
        """
        # Same code as Path Sum II, just check for targetSum backwards before popping
        if not root:
            return 0
        
        current_path = []
        
        global res
        res = 0
        
        def dfs(node, current_sum, current_path):
            global res
            
            if not node:
                return

            current_path.append(node.val)

            # Start checking from back in each unique path, if targetSum is achieved
            
            # Instead of checking at a leaf node, you simply check at 
            # all times if the target has been reached. As soon as it is, 
            # increase the count
            sum = 0

            for index in range(len(current_path) - 1, -1, -1):
                sum += current_path[index]
                if sum == targetSum:
                    res += 1
            
            dfs(node.left, current_sum, current_path) or dfs(node.right, current_sum, current_path)
            
            current_path.pop()
            

        dfs(root, 0, current_path)
        return res
# @lc code=end

