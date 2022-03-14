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
        
        # Working with indices, so can use enumerate
        
        for index, value in enumerate(nums):
            diff = target-value
            
            if diff in dictionary:
                return[index, dictionary[diff]]
            else:
                dictionary[value] = index
            
# @lc code=end

