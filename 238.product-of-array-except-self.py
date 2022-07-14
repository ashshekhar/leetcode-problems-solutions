#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        left_product = [0] * n
        right_product = [0] * n
        output = [0] * n
        
        # Fill left products
        # left_product[i] is product of all nums to the left except nums[i]
        left_product[0] = 1
        
        for i in range(1, len(nums)):
            left_product[i] = left_product[i - 1] * nums[i - 1]
        
        # Fill right products
        # right_product[i] is product of all nums to the right except nums[i]
        right_product[n - 1] = 1
        
        for i in range(n - 2, -1, -1):
            right_product[i] = right_product[i + 1] * nums[i + 1]
            
        # Prepare output array
        for i in range(len(nums)):
            output[i] = left_product[i] * right_product[i]
        
        return output
                   
# @lc code=end