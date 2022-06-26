#
# @lc app=leetcode id=264 lang=python
#
# [264] Ugly Number II
#

# @lc code=start
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        index_2, index_3, index_5 = 0, 0, 0
        
        dp = [0 for _ in range(n)]
        dp[0] = 1
        
        for i in range(1, n):
            # Find the minimum of all ugly numbers generated, each of which are generated based on the last ugly number of that prime
            minimum = min(2 * dp[index_2], 3 * dp[index_3], 5 * dp[index_5])
            
            dp[i] = minimum
            
            if minimum == 2 * dp[index_2]:
                index_2 += 1
         
            if minimum == 3 * dp[index_3]:
                index_3 += 1
            
            if minimum == 5 * dp[index_5]:
                index_5 += 1
        
        return dp[n-1]
            
# @lc code=end

