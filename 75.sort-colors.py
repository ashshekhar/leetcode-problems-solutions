#
# @lc app=leetcode id=75 lang=python
#
# [75] Sort Colors
#

# @lc code=start
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        dictionary = {0:0, 1:0, 2:0}
        index = 0
        
        if len(nums) == 0:
            return nums
        
        for num in nums:
            if num in dictionary:
                dictionary[num] += 1
            else:
                return

        for key, val in dictionary.items():
            for i in range(index, index + val):
                nums[i] = key
                
            index += val
        
        return nums
        
# @lc code=end

