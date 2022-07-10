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
        
        min_heap = []
        
        for stone in stones:
            heapq.heappush(min_heap, -stone)
        
        while len(min_heap) > 1:
            stone_1 = heapq.heappop(min_heap)
            stone_2 = heapq.heappop(min_heap)
            
            if stone_1 != stone_2:
                heapq.heappush(min_heap, stone_1 - stone_2)
        
        return -min_heap[0] if min_heap else 0
        
# @lc code=end

