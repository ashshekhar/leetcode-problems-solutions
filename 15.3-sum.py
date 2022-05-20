#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        output = []
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
                
                if (sum < 0):
                    l+=1
                elif (sum > 0):
                    r -= 1
                else:
                    output.append([value, nums[l], nums[r]]) 
                    l += 1
                    
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        return output
            
# @lc code=end

