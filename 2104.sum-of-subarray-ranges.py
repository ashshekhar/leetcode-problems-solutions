#
# @lc app=leetcode id=2104 lang=python
#
# [2104] Sum of Subarray Ranges
#

# @lc code=start
class Solution(object):
    def subArrayRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # TC: O(n^2)
        sum = 0
        
        for i in range(len(nums)):
            maximum = nums[i]
            minimum = nums[i]
            
            for j in range(i + 1, len(nums)):
                maximum = max(maximum, nums[j])
                minimum = min(minimum, nums[j])
            
                sum += maximum - minimum
                
        return sum
    
        # Try in TC: O(n)
        
# @lc code=end

