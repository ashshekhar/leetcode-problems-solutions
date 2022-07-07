#
# @lc app=leetcode id=40 lang=python
#
# [40] Combination Sum II
#

# @lc code=start
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # This is different than Combination Sum I because this has duplicate values
        # To make sure, we never select duplicates, if we decide to not include a value then ignore ALL the same values
        
        combination = []
        res = []
        
        # Helpful because we only want to use one number once
        candidates.sort()
        
        def backtrack(index):
            
            if sum(combination) == target:
                res.append(combination[::])
                return
            
            if index >= len(candidates) or sum(combination) > target:
                return
            
            # Chose nums[index]
            combination.append(candidates[index])
            backtrack(index + 1)
            
            # Don't choose nums[index]
            combination.pop()
            
            # To make sure, we never select duplicates, if we decide to not include a value then ignore ALL the same values
            while index + 1 < len(candidates) and candidates[index] == candidates[index + 1]:
                index += 1
                
            backtrack(index + 1)
        
        backtrack(0)
        return res
        
# @lc code=end

