#
# @lc app=leetcode id=16 lang=python
#
# [16] 3Sum Closest
#

# @lc code=start
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        min_diff = float("inf")
        nums.sort()
        
        # [-1, 0, 1, 2, -1, -4]
        # [-4, -1, -1, 0, 1, 2]
        
        for index, value in enumerate(nums):
            
            if index > 0 and value == nums[index-1]:
                continue
            
            l = index + 1
            r = len(nums)-1
            
            while l < r:
                sum = value + nums[l] + nums[r]
                
                diff = abs(sum - target)
                
                # Found a closer sum to the target, update res
                if diff < min_diff:
                    res = sum
                    min_diff = diff

                if (sum < target):
                    l+=1
                    
                elif (sum > target):
                    r -= 1
                
                # Else find the next unique triplet
                else:
                    l += 1
                    
                    # To avoid duplicate triplets while 'value' is fixed
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                        
                # Diff == 0, hence the closest sum so break
                if diff == 0:
                    break
        
        return res
        
# @lc code=end

