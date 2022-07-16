#
# @lc app=leetcode id=162 lang=python
#
# [162] Find Peak Element
#

# @lc code=start
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        
        if nums[0] > nums[1]:
            return 0
        
        elif nums[len(nums) - 1] > nums[len(nums) - 2]:
            return len(nums) - 1

        # Binary Search
        left = 1
        right = len(nums) - 2
        
        while left <= right:
            mid = left + (right - left) // 2

            # Found peak element
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid
            
            # We are on left slope, peak on top
            elif nums[mid] < nums[mid + 1]:
                left = mid + 1
                
            # We are on right slope, peak on top
            elif nums[mid] < nums[mid - 1]:
                right = mid - 1
  
# @lc code=end

