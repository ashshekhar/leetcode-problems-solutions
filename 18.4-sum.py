#
# @lc app=leetcode id=18 lang=python
#
# [18] 4Sum
#

# @lc code=start
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        quadruplet = []
        
        nums.sort()
        
        # [-1, 0, 1, 2, -1, -4]
        # [-4, -1, -1, 0, 1, 2]
        
        # Generic KSum
        def kSum(k, start_index, target):
            
            # Non-base Case
            if k != 2:
                
                for i in range(start_index, len(nums) - k + 1):
                    
                    # Skip the same values except first
                    if i >= start_index and nums[i] == nums[i-1]:
                        continue
                    
                    quadruplet.append(nums[i])
                    
                    kSum(k - 1, start_index + 1, target - nums[i])
                    
                    # Stored the result in res, so clean quadruplet
                    quadruplet.pop()

                # To stop the code from executing the below case 
                return
                
            # Base Case: Two Sum II
            left = start_index
            right = len(nums) - 1
            

            while left < right: 
                sum = nums[left] + nums[right]
                
                if sum < target:
                    left += 1
                elif sum > target:
                    right -= 1
                else:
                    # Use the k - 2 values already in quadruplet from the recursive calls 
                    # and 2 found here
                    res.append(quadruplet + [nums[left], nums[right]])  
                    
                    # Skip same values
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                        
        kSum(4, 0, target)
        return res
                            
# @lc code=end

