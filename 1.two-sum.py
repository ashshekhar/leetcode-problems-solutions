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
        dictionary = {}
        
        for index, value in enumerate(nums):
            difference = target - value
            
            if difference not in dictionary:
                dictionary[value] = index
            else:
                return [index, dictionary[difference]]
                
# @lc code=end

