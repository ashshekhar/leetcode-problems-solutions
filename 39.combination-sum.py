#
# @lc app=leetcode id=39 lang=python
#
# [39] Combination Sum
#

# @lc code=start
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        combination = []
        res = []
        
        def backtrack(index):
            
            if sum(combination) == target:
                res.append(combination[::])
                return
            
            if index >= len(candidates) or sum(combination) > target:
                return
            
            # Chose nums[index]
            # Backtracking starts at index itself since you can either choose again or not
            combination.append(candidates[index])
            backtrack(index)
            
            # Don't choose nums[index]
            # Didn't choose, so go to next index
            combination.pop()
            backtrack(index + 1)
        
        backtrack(0)
        return res
        
    
# @lc code=end