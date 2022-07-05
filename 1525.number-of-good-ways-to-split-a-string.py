#
# @lc app=leetcode id=1525 lang=python
#
# [1525] Number of Good Ways to Split a String
#

# @lc code=start
from collections import Counter
class Solution(object):
    def numSplits(self, s):
        """
        :type s: str
        :rtype: int
        """
        left_dict = {}
        right_dict = Counter(s)
        res = 0
        
        for _, value in enumerate(s):
            left_dict[value] = 1 + left_dict.get(value, 0)
            right_dict[value] -= 1
            
            # Can't divide into empty substring
            if right_dict[value] == 0:
                del right_dict[value]

            if len(left_dict) == len(right_dict):
                res += 1
        
        return res
# @lc code=end

