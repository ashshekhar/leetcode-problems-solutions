#
# @lc app=leetcode id=1584 lang=python
#
# [1584] Min Cost to Connect All Points
#

# @lc code=start
import heapq

class Solution(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        n = len(points)
        
        # Map point at each index in points to a list of lists 
        # containing neighbor and distance to that neighbor
        point_dict = {i : [] for i in range(n)}
        
        for i in range(n):
            x1, y1 = points[i]
            
            for j in range(i + 1,  n):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                
                point_dict[i].append([dist, j])
                point_dict[j].append([dist, i]) 
        
        # Prim's Algorithm for MST
        # Add index 0 with cost 0
        min_heap = [[0, 0]]
        visited = set()
        final_cost = 0
        
        # Only visited one node once with it's shortest cost
        while len(visited) < n:

            cost, index = heapq.heappop(min_heap)

            # Since we are adding same nodes multiple times in the heap
            # But only once in visited set
            if index in visited:
                continue
            
            visited.add(index)
            final_cost += cost
            
            for neighbor_cost, neighbor_index in point_dict[index]:
                heapq.heappush(min_heap, [neighbor_cost, neighbor_index])
        
        return final_cost        
    
# @lc code=end

