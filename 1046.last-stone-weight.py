#
# @lc app=leetcode id=1046 lang=python
#
# [1046] Last Stone Weight
#

# @lc code=start
import heapq

class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        if len(stones) == 1:
            return 1
        
        max_heap = []
        
        for stone in stones:
            heapq.heappush(max_heap, -stone)
        
        # At each step, pull out two heaviest stones and store the result
        while len(max_heap) > 1:
            stone_1 = -1 * heapq.heappop(max_heap)
            stone_2 = -1 * heapq.heappop(max_heap)
            
            if stone_1 != stone_2:
                heapq.heappush(max_heap, -(stone_1 - stone_2))
        
        return -max_heap[0] if max_heap else 0
        
# @lc code=end

