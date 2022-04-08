#
# @lc app=leetcode id=287 lang=python
#
# [287] Find the Duplicate Number
#

# @lc code=start
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        duplicate = {}
        
        for num in nums:
            if num in duplicate:
                duplicate[num] += 1
            else:
                duplicate[num] = 1
                    
        for pairs in duplicate.keys():
            if duplicate[pairs] > 1:
                return pairs   
               
        
# @lc code=end

