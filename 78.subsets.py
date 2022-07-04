#
# @lc app=leetcode id=78 lang=python
#
# [78] Subsets
#

# @lc code=start
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        subset = []
        
        def backtrack(index):
            if index >= len(nums):
                res.append(subset[:])
                return
            
            # Decision to add nums[index]
            subset.append(nums[index])
            backtrack(index + 1)
            
            # Decision to not add nums[index]
            subset.pop()
            backtrack(index + 1)
            
        backtrack(0)
        return res
# @lc code=end

