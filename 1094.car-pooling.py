#
# @lc app=leetcode id=1094 lang=python
#
# [1094] Car Pooling
#

# @lc code=start
import heapq

class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        # Sort by start pickup destination
        trips = sorted(trips, key = lambda x:x[1])
        
        current_pass = 0
        min_heap = []
        
        for trip in trips:
            passenger, start, end = trip
            
            # While for the passengers their dest was less than currentstart
            # Drop them and decrease current_pass_in_car
            while min_heap and min_heap[0][0] <=  start:
                current_pass -= min_heap[0][1]
                heapq.heappop(min_heap)
            
            # Else simply add the current    
            current_pass += passenger
            
            # Check if the cap increased, if not then only push
            if current_pass > capacity:
                return False
            
            heapq.heappush(min_heap, (end, passenger))
            
        return True
# @lc code=end

