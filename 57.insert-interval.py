#
# @lc app=leetcode id=57 lang=python
#
# [57] Insert Interval
#

# @lc code=start
class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        result = []
        
        for i in range(len(intervals)):
            
            # We have reached a state where newInterval is non-overlapping with the rest of the intervals
            if newInterval[1] < intervals[i][0]:
                result.append(newInterval)
                return result + intervals[i:]
            
            # Current interval is okay to be added in result
            elif newInterval[0] > intervals[i][1]:
                result.append(intervals[i])
            
            # Recursively create newInterval
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
                        
        result.append(newInterval)            
        return result
                               
# @lc code=end

