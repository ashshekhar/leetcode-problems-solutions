import heapq

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        # So, every time we want to check if any room is free or not, simply check the topmost element of         
        # the min heap as that would be the room that would get free the earliest out of all the other 
        # rooms currently occupied.
        
        # This min_heap stores the end time because that's all we need to see if the room can be free
        min_heap = []
        
        heapq.heapify(min_heap)
        heapq.heappush(min_heap, intervals[0][1])
        
        # Sort based on start time because you would want to schedule earlier start time first
        sorted(intervals, key = lambda x:x[0])
        
        for i in range(1, len(intervals)):
            
            # If the start of the new meeting is before the end of the earliest meeting in assigned rooms
            # Then, you need to add a new meeting room
            if intervals[i][0] <= min_heap[0]:
                heapq.heappush(min_heap, intervals[i][1])
            
            # Else, you can reuse one of the assigned rooms
            else:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, intervals[i][1])
                
        return len(min_heap)
            