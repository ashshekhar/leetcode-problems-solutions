class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        if not intervals:
            return True
        
        intervals = sorted(intervals, key = lambda x:x[1])
        
        last_end_time = intervals[0][1]
        
        for i in range(1, len(intervals)):
            
            if intervals[i][0] < last_end_time:
                return False
            
            else:
                last_end_time = intervals[i][1]
            
        return True