#
# @lc app=leetcode id=287 lang=python
#
# [287] Find the Duplicate Number
#

# @lc code=start
from collections import Counter
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        duplicate = Counter(nums)
        
        for keys in duplicate.keys():
            if duplicate[keys] > 1:
                return keys   
               
        
# @lc code=end

