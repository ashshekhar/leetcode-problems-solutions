#
# @lc app=leetcode id=33 lang=python
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        length = len(nums)
        left = 0
        right = length - 1
        
        if length == 0 or (length == 1 and nums[0] != target):
            return -1
        
        # Very clever use of modified binary search algorithm
        while left <= right:
            
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            
            # Left half sorted
            if nums[mid] >= nums[left]:
                if target <= nums[mid] and target >= nums[left]:
                    right = mid - 1
                else:
                    left = mid + 1
            
            # Right half sorted
            elif nums[mid] < nums[left]:
                if target >= nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return -1       
# @lc code=end

