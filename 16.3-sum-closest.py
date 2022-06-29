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
                
                if diff < min_diff:
                    res = sum
                    min_diff = diff

                if (sum < target):
                    l+=1
                    
                elif (sum > target):
                    r -= 1
                
                # Found the target
                if diff == 0:
                    break
        
        return res
        
# @lc code=end

