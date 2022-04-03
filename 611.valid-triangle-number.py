#
# @lc app=leetcode id=611 lang=python
#
# [611] Valid Triangle Number
#

# @lc code=start
from collections import Counter

class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        count = 0
        
        for i in range(2, len(nums)):
            left = 0
            right = i-1
            
            while(left < right): 
                
                if nums[left] + nums[right] > nums[i]:
                    count += right-left
                    right -= 1

                else:
                    left += 1
                    
        return count
# @lc code=end

