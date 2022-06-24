#
# @lc app=leetcode id=27 lang=python
#
# [27] Remove Element
#

# @lc code=start
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # You don't have to shift every val, just swap the first val element 
        # and the first non-val element once
        
        # [2, 1, 2, 3, 4]; target = 2
        
        # [1, 2, 2, 3, 4]
        
        # [1, 3, 2, 2, 4]
        
        # [1, 3, 4, 2, 2]
        
        length = len(nums)
        
        current_val_pos = 0
        
        for i in range(length):

            if nums[i] != val:
                nums[current_val_pos], nums[i] = nums[i], nums[current_val_pos]
                current_val_pos += 1
                
        return current_val_pos
# @lc code=end

