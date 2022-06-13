#
# @lc app=leetcode id=215 lang=python
#
# [215] Kth Largest Element in an Array
#

# @lc code=start
import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # These approaches work when you want the kth largest element
        # Not the kth largest distinct element
        
        # Using built-in sorted
        # nums = sorted(nums, reverse = True)
        # return nums[k-1]
        
        # Using max-heap: Pop k-2 times to get the answer
        max_heap = []
        heapq.heapify(max_heap)
        
        for num in nums:
            heapq.heappush(max_heap, -1 * num)
            
        for _ in range(k-1):
            heapq.heappop(max_heap)

        return -1 * max_heap[0]
        
    
# @lc code=end

