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
        right_product = [0 for i in range(len(nums))]
        output = []
        
        left_product.append(1)
        right_product.insert(len(nums)-1, 1)
        
        for i in range(1, len(nums)):
            left_product.append(left_product[i-1] * nums[i-1])  
            
        for i in range(len(nums)-2, -1, -1):
            right_product[i] = right_product[i+1] * nums[i+1]

        for i in range(len(nums)):
            output.append(left_product[i] * right_product[i])
        
        return output
            
# @lc code=end