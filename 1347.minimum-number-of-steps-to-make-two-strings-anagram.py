#
# @lc app=leetcode id=1347 lang=python
#
# [1347] Minimum Number of Steps to Make Two Strings Anagram
#

# @lc code=start
from collections import Counter
class Solution(object):
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        s_dict, steps = Counter(s), 0
        
        for char in t:
            
            # Can use
            if s_dict[char] > 0:
                s_dict[char] -= 1
            
            # Else need replacement
            else:
                steps += 1
                
        return steps
        
        
# @lc code=end

