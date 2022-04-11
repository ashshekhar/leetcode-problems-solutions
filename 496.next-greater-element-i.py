#
# @lc app=leetcode id=496 lang=python
#
# [496] Next Greater Element I
#

# @lc code=start
from collections import deque

class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # The idea is that you append a number in the stack only when the top
        # element is larger. If smaller then for that smaller top, num is the next bigger.
        # Therefore, use a dictionary to map that smaller element to num.
        
        monotonic_stack = []
        mapping = {}
        result = []
        
        for num in nums2:
            while monotonic_stack and num > monotonic_stack[-1]:
                mapping[monotonic_stack.pop()] = num
                
            monotonic_stack.append(num)
        
        for num in nums1:
            if num in mapping.keys():
                result.append(mapping[num])
            else:
                result.append(-1)
                
        return result
                        
# @lc code=end

