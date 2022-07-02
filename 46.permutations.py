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
        
        # When you return back for next iteration, the first element to be popped will now 
        # be the second element in origianl list, because of the way we have written the function
        
        # [1, 2, 3] (pop 1) -> [2, 3] (pop 2) -> [3] (base case) -> [3, 2] (append back 2) and (pop 3) 
        # -> [2] -> [2, 3] (add back 3) -> [2, 3, 1]; [3, 2, 1] (append back 1 for both the permutations)
        
        # Continue the same with [2, 3, 1] as your original array now
        for i in range(len(nums)):
            
            # Pop the element at index 0
            num = nums.pop(0)
            permutations = self.permute(nums)
            
            # Add back the element popped above in result
            for permutation in permutations:
                permutation.append(num)
            
            result.extend(permutations)
            
            # Add back num in the end of the nums array, for next iteration
            nums.append(num)
        
        return result
# @lc code=end

