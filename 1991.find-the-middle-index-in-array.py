#
# @lc app=leetcode id=1991 lang=python
#
# [1991] Find the Middle Index in Array
#

# @lc code=start
class Solution(object):
    def findMiddleIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_sum = sum(nums)
        left_sum = 0
        
        for i in range(len(nums)):
            if left_sum == total_sum - nums[i] - left_sum:
                return i
            left_sum += nums[i]
                
        return -1
# @lc code=end

