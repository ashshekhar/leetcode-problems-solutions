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
        left_product = []
        right_product = []
        output = []
        
        for i in range(len(nums)):
            left_product.append(0)
            right_product.append(0)
            output.append(0)
        
        # Fill left products
        left_product[0] = 1
        
        for i in range(len(nums) - 1):
            left_product[i+1] = left_product[i] * nums[i]
        
        # Fill right products
        right_product[len(nums) - 1] = 1
        
        for i in range(len(nums) - 1, 0, -1):
            right_product[i-1] = nums[i] * right_product[i]
            
        # Prepare output array
        for i in range(len(nums)):
            output[i] = left_product[i] * right_product[i]
        
        return output
                   
# @lc code=end