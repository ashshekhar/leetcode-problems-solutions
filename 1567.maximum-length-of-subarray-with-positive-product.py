#
# @lc app=leetcode id=1567 lang=python
#
# [1567] Maximum Length of Subarray With Positive Product
#

# @lc code=start
class Solution(object):
    def getMaxLen(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        # pos[i] tells you the maximum length of a positive product including ith index
        pos = [0] * len(nums)
        
        # neg[i] tells you the maximum length of a negative product including ith index
        neg = [0] * len(nums)

        if nums[0] > 0:
            pos[0] = 1
        elif nums[0] < 0:
            neg[0] = 1
        
        # Base case
        res = pos[0]
        
        # A positive value will only increment the length of both arrays
        # A negative value will increment basd on the length of the other array
        for i in range(1, len(nums)):
            if nums[i] > 0:
                
                # Pos length always increments by 1
                pos[i] = 1 + pos[i - 1]
                
                # If neg length existed before, a new positive will increment the length by 1
                if neg[i - 1] > 0: 
                    neg[i] = 1 + neg[i - 1]
            
            elif nums[i] < 0:
                
                # If no neg existed, then length of neg will be 1 + positive length from before
                neg[i] = 1 + pos[i - 1]
                
                # If neg existed before, then pos length increments by 1
                if neg[i - 1] > 0:
                    pos[i] = 1 + neg[i - 1]
            
            # Store the max length
            res = max(res, pos[i])
    
        return res
# @lc code=end

