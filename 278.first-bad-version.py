#
# @lc app=leetcode id=278 lang=python
#
# [278] First Bad Version
#

# @lc code=start
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):  
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        
        while left <= right:
            mid = (left + right) // 2
            
            if isBadVersion(mid) and not isBadVersion(mid - 1):
                return mid
            
            elif isBadVersion(mid):
                right = mid - 1
                
            else:
                left = mid + 1
        
        return left
# @lc code=end

