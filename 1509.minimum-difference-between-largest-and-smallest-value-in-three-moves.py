#
# @lc app=leetcode id=1509 lang=python
#
# [1509] Minimum Difference Between Largest and Smallest Value in Three Moves
#

# @lc code=start
import heapq

class Solution(object):
    def minDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """      
        # Given 0 move: min(0 + 1 difference)  = min (1 largest - 1 smallest)
        # Given 1 moves: min(1 + 1 difference) = min (2 largest - 2 smallest)
        
        # If length <= 4: Can always make all the numbers equal
        if len(nums) < 5:
            return 0
        
        heapq.heapify(nums)
        largest = heapq.nlargest(4, nums)[::-1]
        smallest = heapq.nsmallest(4, nums)

        return min([large - small for large, small in zip(largest, smallest)])   
# @lc code=end

