#
# @lc app=leetcode id=46 lang=python
#
# [46] Permutations
#

# @lc code=start
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        
        # Nested array format
        if len(nums) == 1:
            return [nums[:]]
        
        # For each element, pop it and find all permutations of the remaining elements
        for i in range(len(nums)):
            
            # Pop the element at index 0
            num = nums.pop(0)
            permutations = self.permute(nums)
            
            # Add back the popped element in result
            for permutation in permutations:
                permutation.append(num)
            
            result.extend(permutations)
            
            # Add back num in the end of the nums array, for next iteration
            nums.append(num)
        
        return result
# @lc code=end

