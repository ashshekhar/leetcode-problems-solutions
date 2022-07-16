#
# @lc app=leetcode id=45 lang=python
#
# [45] Jump Game II
#

# @lc code=start
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # nums -> [2,3,1,1,4]
        # dp -> [2, 1, 2, 1, 0]
        # dp[i] represents the minimum number of steps to take from ith index to reach end
        dp = [float("inf") for _ in range(len(nums))]
        
        # Base Case
        dp[len(nums) - 1] = 0

        for i in reversed(range(len(nums) - 1)):
            minimum = float("inf")
            
            # Since we don't need to necessarily jump the max possible at each index
            # So start with 1 to max val allowed and check which value < num[i] yields least jumps
            for j in range(1, nums[i] + 1):
                if i + j < len(nums):
                    minimum = min(minimum, dp[i + j])
                
            dp[i] = 1 + minimum
        
        print(dp)
        return dp[0]
        
# @lc code=end

