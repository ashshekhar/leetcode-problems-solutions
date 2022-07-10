#
# @lc app=leetcode id=1438 lang=python
#
# [1438] Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
#

# @lc code=start
from collections import deque
class Solution(object):
    def longestSubarray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        # To get the max and min of a window in O(1)
        incr_queue = deque()
        decr_queue = deque()
        
        i = 0
        res = 0
        
        for j in range(len(nums)):
            
            # Update the queues to get the max and min correctly
            while incr_queue and incr_queue[-1] > nums[j]:
                incr_queue.pop()
            incr_queue.append(nums[j])
            
            while decr_queue and decr_queue[-1] < nums[j]:
                decr_queue.pop()
            decr_queue.append(nums[j])
        
            # If the window (i, j) doesn't follow the rule, increase i
            while decr_queue[0] - incr_queue[0] > limit:
                if incr_queue[0] == nums[i]:
                    incr_queue.popleft()
                    
                elif decr_queue[0] == nums[i]:
                    decr_queue.popleft()

                i += 1
            
            res = max(res, j - i + 1)

        return res
# @lc code=end

