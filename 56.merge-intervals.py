#
# @lc app=leetcode id=56 lang=python
#
# [56] Merge Intervals
#

# @lc code=start
from calendar import c


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        output = []
        intervals = sorted(intervals, key=lambda x:x[0])
        
        if len(intervals) == 1:
            return intervals
        
        current_interval = intervals[0]
        output.append(current_interval)
        
        for i in range(1, len(intervals)):
            current_end = current_interval[1]
            next_begin = intervals[i][0]
            
            # Gets updated in output
            if next_begin <= current_end:
                current_interval[0] = min(current_interval[0], intervals[i][0])
                current_interval[1] = max(current_interval[1], intervals[i][1])

            # No overlap, simply update the current_interval to current
            else:
                current_interval = intervals[i]
                output.append(current_interval)
        
        return output 
# @lc code=end

