#
# @lc app=leetcode id=1492 lang=python
#
# [1492] The kth Factor of n
#

# @lc code=start
from operator import le


class Solution(object):
    def kthFactor(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        factor_list = []
        
        for i in range(1, n+1):
            if n%i == 0:
                factor_list.append(i)
        
        if k > len(factor_list):
            return -1
        
        return factor_list[k-1]
# @lc code=end

