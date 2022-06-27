#
# @lc app=leetcode id=1423 lang=python
#
# [1423] Maximum Points You Can Obtain from Cards
#

# @lc code=start
class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        max_sum = sum(cardPoints[:k])
        final_max = max_sum
        
        left_ptr = k - 1
        right_ptr = len(cardPoints) - 1        
        
        # Add from end, subtract from left window
        while left_ptr >= 0 and right_ptr < len(cardPoints):
            
            max_sum = max_sum - cardPoints[left_ptr] + cardPoints[right_ptr]
            final_max = max(final_max, max_sum)

            left_ptr -= 1
            right_ptr -= 1
        
        return final_max
        
# @lc code=end

