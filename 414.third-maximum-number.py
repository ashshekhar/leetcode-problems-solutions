#
# @lc app=leetcode id=414 lang=python
#
# [414] Third Maximum Number
#

# @lc code=start
import heapq

class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Based on kth largest element but distinct
        # Max Heap Approach
        nums = list(set(nums))
        length = len(nums)
        
        if length == 1:
            return nums[0]
        
        if length == 2:
            return max(nums)
        
        max_heap = []
        heapq.heapify(max_heap)
        
        for num in nums:
            heapq.heappush(max_heap, -1 * num)
    
            
        for _ in range(2):
            heapq.heappop(max_heap)

        return -1 * max_heap[0]
    
        # Set approach
        # nums = list(set(nums))
        # length = len(nums)
        
        # print(nums)
        # if length == 1:
        #     return nums[0]
        
        # if length == 2:
        #     return max(nums)
        
        # for i in range(2):
        #     nums.remove(max(nums))
            
        # return max(nums)
        
# @lc code=end

