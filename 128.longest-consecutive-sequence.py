#
# @lc app=leetcode id=128 lang=python
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Consecutive sequence means that the numbers increase by 1 in the answer
        if not nums:
            return 0
        
        # Converting to set for efficient lookup
        nums = set(nums)
        current_max = 0
        final_max = 0

        for num in nums:
            temp = num
            current_max = 0
            
            # This condition gives us the start of the longest consecutive sequence
            if num - 1 not in nums and num + 1 in nums:
                while temp in nums:
                    current_max += 1
                    temp += 1
            else:
                current_max = 1
                
            final_max = max(final_max, current_max)
                
        return final_max
# @lc code=end

