#
# @lc app=leetcode id=347 lang=python
#
# [347] Top K Frequent Elements
#

# @lc code=start
from collections import Counter
import heapq

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        nums = Counter(nums)
        heap = []
        res = []
        
        for key, value in nums.items():
            heapq.heappush(heap, ( -1 * value, key))
            
        while k > 0:
            res.append(heapq.heappop(heap)[1])
            k -= 1
            
        return res
            
# @lc code=end

