#
# @lc app=leetcode id=503 lang=python
#
# [503] Next Greater Element II
#

# @lc code=start
from collections import deque


class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        monotonic_stack = []
        mapping = dict()
        output = []
        length = len(nums)
        
        for i in range(0, length*2):            
            while monotonic_stack and nums[i%length] > monotonic_stack[-1]: 
                pop_val = monotonic_stack.pop()
                
                if pop_val in mapping:
                    mapping[pop_val].append(nums[i%length])
                else:
                    mapping[pop_val] = deque([nums[i%length]])
        
            monotonic_stack.append(nums[i%length])

        for num in nums:
            if num in mapping.keys():
                output.append(mapping[num].popleft())
            else:
                output.append(-1)
    
        return output
        
# @lc code=end

