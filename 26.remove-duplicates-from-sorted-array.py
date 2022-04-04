#
# @lc app=leetcode id=26 lang=python
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Let left pointer denote the spot where the new unique element comes in
        left = 1
        right = 1
        
        # Compare the value pointed by right pointer to previous element
        while right < len(nums):
            if nums[right] == nums[right-1]:
                right += 1
            else:
                nums[left] = nums[right]
                left += 1 
                right += 1
                
        return left
            
# @lc code=end

