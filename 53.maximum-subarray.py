#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Kadane's Algorithm
        max_so_far = 0
        final_max = float('-inf')

        for i in range(len(nums)):
            max_so_far += nums[i]
            
            final_max = max(final_max, max_so_far)

            if max_so_far < 0:
                max_so_far = 0
            
        return final_max
# @lc code=end