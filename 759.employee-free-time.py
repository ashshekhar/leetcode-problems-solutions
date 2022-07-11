
# Definition for an Interval.
class Interval(object):
    def __init__(self, start=None, end=None):
        self.start = start
        self.end = end

class Solution(object):
    def employeeFreeTime(self, schedule):
        """
        :type schedule: [[Interval]]
        :rtype: [Interval]
        """
        # Simply sort the intervals based on start time
        # Then find the gaps and add to res
        
        # Sort the nested list based on start val
        intervals = sorted([interval for s in schedule for interval in s], key = lambda x : x.start)
        res = []
        
        end = intervals[0].end
        
        for i in range(1, len(intervals)):
            
            # Gap identified
            if end < intervals[i].start:
                res.append(Interval(end, intervals[i].start))
            
            # Update new end time
            end = max(end, intervals[i].end)
        
        return res