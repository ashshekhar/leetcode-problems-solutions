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
        visit = set()
        
        for num in nums:
            if num not in visit:
                visit.add(num)
            else:
                return num
        
# @lc code=end

