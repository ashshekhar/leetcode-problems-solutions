#
# @lc app=leetcode id=977 lang=python
#
# [977] Squares of a Sorted Array
#

# @lc code=start
import heapq

class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Heapify is O(N)
        ans = []
        nums = [nums[i]**2  for i in range(len(nums))]
        
        heapq.heapify(nums)
        
        while nums:
            ans.append(heapq.heappop(nums))
        
        return ans
# @lc code=end

