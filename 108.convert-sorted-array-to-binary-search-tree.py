#
# @lc app=leetcode id=108 lang=python
#
# [108] Convert Sorted Array to Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def helper(left, right):
            if left > right:
                return None

            # Always choose left middle node as a root
            mid =  (right + left) // 2

            # Preorder traversal: node -> left -> right
            # Need to first create the node, can't do inorder
            root = TreeNode(nums[mid])
            
            root.left = helper(left, mid - 1)
            
            root.right = helper(mid + 1, right)
            
            return root
        
        return helper(0, len(nums) - 1)
        
# @lc code=end

