#
# @lc app=leetcode id=539 lang=python
#
# [539] Minimum Time Difference
#

# @lc code=start
class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        # Convert each string to minutes after midnight
        for index, time in enumerate(timePoints):
            hour, minute = time.split(":")
            timePoints[index] = int(hour) * 60 + int(minute)
        
        # Sort
        timePoints = sorted(timePoints)
        
        # Initialize the result
        # Need to consider the first and last diff too
        # Diff of "00:00" and "23:59" is 1
        
        res = 1440 + (timePoints[0] - timePoints[-1])
        
        for i in range(1, len(timePoints)):
            res = min(res, (timePoints[i] - timePoints[i-1]))
    
        return res

# @lc code=end

