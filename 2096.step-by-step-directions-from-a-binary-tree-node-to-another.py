#
# @lc app=leetcode id=2096 lang=python
#
# [2096] Step-By-Step Directions From a Binary Tree Node to Another
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getDirections(self, root, startValue, destValue):
        """
        :type root: Optional[TreeNode]
        :type startValue: int
        :type destValue: int
        :rtype: str
        """
        
        global res, left, right
        res = []
        
        final_s = []
        final_t = []
        
        left = "L"
        right = "R"
        
        def preorder(node, target, path, final_path, to_append):

            if not node:
                return False

            if node.val == target:
                path.append(to_append)
                final_path.append(path[::])
                
            else:
                path.append(to_append)
            
            preorder(node.left, target, path, final_path, left)
            preorder(node.right, target, path, final_path, right)
            
            path.pop()

        # The idea is that we find paths for both start and target nodes.
        preorder(root, startValue, [], final_s, "")  
        preorder(root, destValue, [], final_t, "")
        
        # Returned as a list of list, so take the first and only element and pop first empty char
        final_s[0].pop(0)
        final_t[0].pop(0)

        # Once we have found them we reduce paths to a lowest common parent node.
        while final_s[0] and final_t[0] and final_s[0][0] == final_t[0][0]:
            final_s[0].pop(0)
            final_t[0].pop(0)
            
        # We change the all items in path of start to 'U' and keep the path of target same.
        return 'U' * len(final_s[0]) + ''.join(final_t[0])
                
        
# @lc code=end

