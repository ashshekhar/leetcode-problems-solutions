#
# @lc app=leetcode id=77 lang=python
#
# [77] Combinations
#

# @lc code=start
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        combinations = [] 
        
        global res
        res = []
        
        nums = [i for i in range(1, n + 1)]
        
        def backtrack(index):
            global res
            
            if len(combinations) == k:
                res.append(combinations[::])
                return
                
            elif index >= len(nums) or len(combinations) > k:
                return
            
            combinations.append(nums[index])
            backtrack(index + 1)
            
            combinations.pop()
            backtrack(index + 1)
            
        
        backtrack(0)
        return res
# @lc code=end

