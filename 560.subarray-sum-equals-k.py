#
# @lc app=leetcode id=560 lang=python
#
# [560] Subarray Sum Equals K
#

# @lc code=start
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Sliding window can't be used because we have negative values
        # For each num added to current_sum, see if previously it was possible to
        # get the diff of current_sum and the target, and if yes, in how many ways?
         
        # Dictionary for possible sums before
        prefix_sum = {}
        prefix_sum[0] = 1
        
        res = 0
        current_sum = 0
        
        for num in nums:
            current_sum += num
            diff = current_sum - k
            
            # Add to result, if it was possible to get the sum k
            res += prefix_sum.get(diff, 0)
            
            # Regardless, add to dictionary for number of ways to get current_sum
            prefix_sum[current_sum] = 1 + prefix_sum.get(current_sum, 0)

        return res
            
# @lc code=end

