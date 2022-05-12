#
# @lc app=leetcode id=532 lang=python
#
# [532] K-diff Pairs in an Array
#

# @lc code=start
from collections import Counter

class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        left_ptr = 0
        right_ptr = 1
        
        counter = Counter(nums)
        
        nums = sorted(list(set(nums)))
        new_length = len(nums)
        
        if k == 0:
            for _, val in counter.items():
                if val >= 2: 
                    count += 1
            return count

        while left_ptr <= right_ptr and right_ptr < new_length:
            diff = nums[right_ptr] - nums[left_ptr]
            
            if  diff == k:
                count += 1
                left_ptr += 1
                right_ptr += 1
                
            elif diff > k:
                left_ptr += 1
            
            else:
                right_ptr += 1
            
        return count
# @lc code=end

