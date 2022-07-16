#
# @lc app=leetcode id=55 lang=python
#
# [55] Jump Game
#

# @lc code=start
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # The idea is to be Greedy and shift the goal post towards the start index
        goal = len(nums) - 1
        
        for i in reversed(range(len(nums))):
            
            # This means you can reach the goal from the current index
            # because nums[i] + i is bigger than the target index
            if i + nums[i] >= goal:
                goal = i
        
        return goal == 0
                
        
# @lc code=end

