#
# @lc app=leetcode id=90 lang=python
#
# [90] Subsets II
#

# @lc code=start
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        res = []
        subset = []

        # This will help us ignore the duplicates
        # To make sure, we never select duplicates, if we decide to not include a value then ignore ALL the same values
        nums.sort()
        
        def backtrack(index):
            if index >= len(nums):
                res.append(subset[:])
                return
            
            # Decision to add nums[index]
            subset.append(nums[index])
            backtrack(index + 1)
            
            # Decision to not add nums[index] and skip all next values which are equal to nums[index]
            subset.pop()
            
            # To make sure, we never select duplicates, if we decide to not include a value then ignore ALL the same values
            while index + 1 < len(nums) and nums[index] == nums[index + 1]:
                index += 1
    
            backtrack(index + 1)
            
        backtrack(0)
        return res
        
# @lc code=end

