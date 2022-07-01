#
# @lc app=leetcode id=424 lang=python
#
# [424] Longest Repeating Character Replacement
#

# @lc code=start
class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # The idea is that you use a sliding window making sure at each time the window is valid
        # Valid window means:
        # len(window) - count of the most frequent character in the window = number of replacements <= k
        
        left = 0
        count = {}
        res = 0
    
        for right in range(len(s)):
            
            # Maintain counter for sliding window, not entire s
            count[s[right]] = 1 + count.get(s[right], 0)
            
            # Window is not valid, move the left pointer until it is valid
            while (right - left + 1) - max(count.values()) > k:
                
                # Remove the count
                count[s[left]] -= 1
                left += 1
            
            # We will always reach here with a valid window 
            # Ans will be max of the windows
            res = max(res, right - left + 1)
            
        return res
        
# @lc code=end

