#
# @lc app=leetcode id=973 lang=python
#
# [973] K Closest Points to Origin
#

# @lc code=start
import heapq

def distance(point):
    return point[0]**2 + point[1]**2

class Solution(object):

    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """

        # if len(points) <= k:
        #     return points
        
        # elif k == 0:
        #     return []
        
        # # One approach
        # min_heap = []
        # res = []
         
        # for i in range(len(points)):
        #     min_heap.append([distance(points[i]), points[i]])
        
        # heapq.heapify(min_heap)
            
        # while k > 0:
        #     dist, point  = heapq.heappop(min_heap)
        #     res.append([point[0], point[1]])
        #     k -= 1
        
        # return res
        
        # Second cleaner approach
        return heapq.nsmallest(k, points, key = distance)
# @lc code=end

