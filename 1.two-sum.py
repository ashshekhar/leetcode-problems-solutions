#
# @lc app=leetcode id=1 lang=python
#
# [1] Two Sum
#

# @lc code=start
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        output = []
        
        for i in range(len(nums)):
            if((target-nums[i]) in nums[i+1:]):
                output.append(i)
                output.append(nums[i+1:].index(target-nums[i]) + (i+1))
                
        return output
# @lc code=end

