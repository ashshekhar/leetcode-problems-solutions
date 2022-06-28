#
# @lc app=leetcode id=153 lang=python
#
# [153] Find Minimum in Rotated Sorted Array
#

# @lc code=start
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        smallest = nums[0]
        
        for i in range(length - 1):
            if nums[i] > nums[i + 1]:
                smallest = nums[i + 1]
                
        return smallest        
# @lc code=end

