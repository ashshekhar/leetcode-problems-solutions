#
# @lc app=leetcode id=47 lang=python
#
# [47] Permutations II
#

# @lc code=start
from collections import Counter

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        permutation = []
        
        count = Counter(nums)
        
        def dfs():
            if len(permutation) == len(nums):
                res.append(permutation[::])
                return
            
            for unique_num in count:
                if count[unique_num] > 0:
                    permutation.append(unique_num)
                    count[unique_num] -= 1
                    
                    dfs()
                    
                    count[unique_num] += 1
                    permutation.pop()
        
        dfs()
        return res            
# @lc code=end

