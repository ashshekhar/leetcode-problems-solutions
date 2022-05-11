#
# @lc app=leetcode id=387 lang=python
#
# [387] First Unique Character in a String
#

# @lc code=start
from collections import OrderedDict

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = OrderedDict()
        i = 0
        
        for ele in s:
            if ele not in count:
                count[ele] = 1
            else:
                count[ele] += 1

        print(count)
        for key, val in count.items():
            print(key, val)
            if val == 1:
                return s.index(key)
                  
        return -1
# @lc code=end

