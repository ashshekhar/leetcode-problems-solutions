#
# @lc app=leetcode id=189 lang=python
#
# [189] Rotate Array
#

# @lc code=start
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # Avoid redundant work
        length = len(nums)
        
        if k >= length:
            k = k % length
        
        # Brute force approach with time limit exceeded
        # for _ in range(k):
        #     temp = nums[:]
            
        #     for i in range(len(nums)):
        #         nums[i] = 0
                
        #     nums[0] = temp[len(nums) - 1]
            
        #     for i in range(len(temp) - 1):
        #         nums[i+1] = temp[i]

        # Smarter approach: Swap the two halves
        # nums[a:b] is inclusive of a and exclusive of b
        nums[k: ], nums[ :k] = nums[ :-k], nums[-k: ]
        
# @lc code=end

