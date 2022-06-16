#
# @lc app=leetcode id=658 lang=python
#
# [658] Find K Closest Elements
#

# @lc code=start
import heapq

class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        # Min heap extracts min most based on first element of tuple
        res = []
        
        heap = []
        heapq.heapify(heap)

        for num in arr:
            heapq.heappush(heap, [abs(x - num), num])

        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        
        res = sorted(res)
        return res
            
            
        
# @lc code=end

