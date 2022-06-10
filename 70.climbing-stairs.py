#
# @lc app=leetcode id=70 lang=python
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Important concept is that the question is not asking for how many steps but rather ways
        # So if you want to climb nth stair, you can either take 1 step from n-1 th stair or 2 from n-2 th stair
        # So the total number of ways to climb the nth chair would be their sum
        
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        # DP Array approach
        dp = [0] * n
        dp[0] = 1
        dp[1] = 2
        
        for i in range(2, n):
            dp[i] = dp[i-1] + dp[i-2]
            
        return dp[n-1]
        
        # Naive Recursive approach
        return self.climbStairs(n-1) + self.climbStairs(n-2)
        
        
# @lc code=end

