#
# @lc app=leetcode id=198 lang=python
#
# [198] House Robber
#

# @lc code=start
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        dp = [0] * length
        
        if length == 0:
            return 0
        elif length == 1:
            return nums[0]
        else:
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])
            
        for i in range(2, length):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        
        return max(dp)
        
# @lc code=end

