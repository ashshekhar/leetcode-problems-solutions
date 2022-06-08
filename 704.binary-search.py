#
# @lc app=leetcode id=704 lang=python
#
# [704] Binary Search
#

# @lc code=start
class Solution(object):
    
    def binary_search(self, nums, target, left, right):
        
        if left > right:
            return -1
        
        mid = (left + right ) // 2

        if nums[mid] == target:
            return mid
        
        if target > nums[mid]:
            return self.binary_search(nums, target, mid + 1, right)
        else:
            return self.binary_search(nums, target, left, mid - 1)
        
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # Basic approach
        # if target in nums:
        #     return nums.index(target)
        
        # return -1
    
        # Harder Approach
        return self.binary_search(nums, target, 0, len(nums) - 1)
        
# @lc code=end

