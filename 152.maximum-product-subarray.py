#
# @lc app=leetcode id=152 lang=python
#
# [152] Maximum Product Subarray
#

# @lc code=start
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        max_so_far = final_max = nums[0]
        min_so_far = final_min = nums[0]

        for i in range(1, length):
            values = [nums[i], nums[i] * max_so_far, nums[i] * min_so_far]
            
            max_so_far = max(values)
            min_so_far = min(values)
            
            final_max = max(final_max, max_so_far)
            final_min = min(final_min, min_so_far)
            
        return final_max
           
# @lc code=end

