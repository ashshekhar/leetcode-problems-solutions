#
# @lc app=leetcode id=347 lang=python
#
# [347] Top K Frequent Elements
#

# @lc code=start
from collections import Counter
import collections

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        nums = Counter(nums)
        nums = collections.OrderedDict(sorted(nums.items(), key=lambda x: x[1], reverse=True))
        
        freq = list()
        
        i = 0
        for key in nums.keys():
            print(key)
            if i < k:
                freq.append(key)
            i += 1
        
        return freq
# @lc code=end

