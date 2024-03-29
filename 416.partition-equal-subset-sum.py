#
# @lc app=leetcode id=416 lang=python
#
# [416] Partition Equal Subset Sum
#

# @lc code=start

class Solution(object):
    
    # Top down approach with memoization in cache
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total = sum(nums)
        
        if total % 2 != 0:
            return False
        
        memo = [[None for _ in range(total // 2 + 1)] for _ in range(len(nums))]

        def recursion(index, target):
            if index >= len(nums) or target < 0:
                return False
            
            # Already cached
            if memo[index][target] != None:
                return memo[index][target]

            # Reached target
            if target == 0:
                return True
            
            res = recursion(index + 1, target) or recursion(index + 1, target - nums[index])
            
            memo[index][target] = res
            return res
            
        return recursion(0, total // 2)
    
    # Tricky DP approach
    # def canPartition(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: bool
    #     """
    #     total = sum(nums)
        
    #     if total % 2 != 0:
    #         return False 
        
    #     # This will contain all possible sums the array can generate
    #     possible_sums = set()
    #     possible_sums.add(0)
        
    #     for i in range(len(nums)):
    #         nextDP = set()
            
    #         for numbers in possible_sums:
    #             nextDP.add(numbers)
    #             nextDP.add(nums[i] + numbers)
                
    #         possible_sums = nextDP
          
    #     return total // 2 in possible_sums
# @lc code=end

