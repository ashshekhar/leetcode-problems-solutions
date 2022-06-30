#
# @lc app=leetcode id=1642 lang=python
#
# [1642] Furthest Building You Can Reach
#

# @lc code=start
import heapq

class Solution(object):
    def furthestBuilding(self, heights, bricks, ladders):
        """
        :type heights: List[int]
        :type bricks: int
        :type ladders: int
        :rtype: int
        """
        # Min-heap
        ladder_allocations = []

        for i in range(len(heights) - 1):
            
            # If no climb is needed
            climb =  heights[i + 1] - heights[i]
            
            if climb <= 0:
                continue
            
            # If climb is needed, then use all of the ladders first, one by one
            # This denotes that 'climb' was covered by a ladder
            heapq.heappush(ladder_allocations, climb)        
            
            # If we end up overusing ladders, so remove the smallest climb and replace with bricks
            if len(ladder_allocations) > ladders:
                remove_ladder = heapq.heappop(ladder_allocations)
                bricks -= remove_ladder
                
                # This is the last we can reach
                if bricks < 0:
                    return i
        
        # If we are here, then bricks were never negative and all ladders were used
        # All houses were covered under conditions
        return len(heights) - 1
                
        
        
# @lc code=end

