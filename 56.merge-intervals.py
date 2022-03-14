#
# @lc app=leetcode id=56 lang=python
#
# [56] Merge Intervals
#

# @lc code=start
from numpy import sort


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        output = []
        intervals = sorted(intervals, key=lambda x:x[0])
        
        current_interval = intervals[0]
        output.append(current_interval)
        
        for interval in intervals:
            current_end = current_interval[1]
            next_begin = interval[0]

            if next_begin <= current_end:
                current_interval[0] = min(current_interval[0], interval[0])
                current_interval[1] = max(current_interval[1], interval[1])
                
            else:
                current_interval = interval
                output.append(current_interval)
        
        return output           
        
# @lc code=end

