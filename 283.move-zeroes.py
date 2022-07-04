#
# @lc app=leetcode id=283 lang=python
#
# [283] Move Zeroes
#

# @lc code=start
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # You don't have to shift every 0, just swap the first 0 and non-zero element once
        length = len(nums)
        
        if length == 1:
            return nums

        # Assume 0 is always at first index, even if it is not
        current_0_pos = 0
        
        for i in range(length):
            if nums[i] != 0:
                nums[current_0_pos], nums[i] = nums[i], nums[current_0_pos]
                current_0_pos += 1
            
# @lc code=end

