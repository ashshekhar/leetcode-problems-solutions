#
# @lc app=leetcode id=435 lang=python
#
# [435] Non-overlapping Intervals
#

# @lc code=start
class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        count = 0
        intervals = sorted(intervals, key = lambda x: x[1])

        # Starting case
        last_end_time = intervals[0][1]
        
        for i in range(1, len(intervals)):
            
            # Overlap case
            if intervals[i][0] < last_end_time:
                count += 1
                
                # Maintain the last_end_time as the min out of two endings
                # Because later ending might overlap more and increase counts
                last_end_time = min(last_end_time, intervals[i][1])

            # Else if not overlapping then move the last_end_time to the 
            # longer non_overlapping for future comparisons, which is the intervals[i][1]
            else:
                last_end_time = intervals[i][1]
                
        return count    
        
# @lc code=end

