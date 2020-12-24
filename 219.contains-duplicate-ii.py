#
# @lc app=leetcode id=219 lang=python
#
# [219] Contains Duplicate II
#

# @lc code=start
from collections import deque

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        k_nearby = deque()
        
        for i in range(1, k+1):
            if(k < len(nums)):
                k_nearby.append(nums[i])

        if (not k_nearby and k>=len(nums)):
            for i in range(1, len(nums)):
                k_nearby.append(nums[i])

        for i in range(len(nums)):
            if(nums[i] in k_nearby):
                return True
            else:
                if(k_nearby):
                    k_nearby.popleft()
                else:
                    return False
                if(i+k+1 < len(nums)):
                    k_nearby.append(nums[i+k+1])
        return False
# @lc code=end

