#
# @lc app=leetcode id=213 lang=python
#
# [213] House Robber II
#

# @lc code=start
class Solution(object):
    def house_rob_1(self, nums):
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
        
        # Base Case
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2, length):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        
        return max(dp)
    
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        
        # Same code as House Robber I but you can't rob the start and end houses at the same time
        # So call helper twice, with first and without last and vice versa.
        return max(self.house_rob_1(nums[ : len(nums) - 1]), self.house_rob_1(nums[1: len(nums)]))
        
# @lc code=end

