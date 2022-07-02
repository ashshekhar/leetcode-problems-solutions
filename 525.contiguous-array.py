#
# @lc app=leetcode id=525 lang=python
#
# [525] Contiguous Array
#

# @lc code=start
class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = {}
        res = 0
        total = 0
        
        for index, value in enumerate(nums):
            # Counting 0 as -1 sum
            if value == 0:
                total -= 1 
            else:
                total += 1
            
            # Tracking the sums we have found and at what max index
            if total not in sum:
                sum[total] = index
            
            # Now if total is 0, that means till index from 0, 1's and 0's are equal 
            if total == 0:
                res = max(res, index + 1)
                
            # Else if we already have this sum encountered before
            # That means, right after the index at which this sum was encountered before, 
            # the number of 1's and 0's are equal
            else:
                res = max(res, index - sum.get(total))
                
        return res
            
# @lc code=end

