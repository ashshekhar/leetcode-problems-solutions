#
# @lc app=leetcode id=746 lang=python
#
# [746] Min Cost Climbing Stairs
#

# @lc code=start
class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        if len(cost) <= 2:
            return min(cost)
        
        # Min you have to pay to climb the ith stair plus reach this stair from start
        dp = [0] * len(cost)
        
        # Base Cases
        # You can start from either
        dp[0] = cost[0]
        
        # This won't be min(cost[0], cost[1]) because if you ever are at step 1, 
        # you have to at least pay cost[1] to climb further
        # So why not just pay cost[1]
        dp[1] = cost[1]
        
        # cost[i] is added because to climb the ith stair, you'll need to at least pay cost[i]
        # So pay that and see which cost is min to reach this ith
        for i in range(2, len(cost)):
            dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])
        
        return min(dp[-1], dp[-2])
# @lc code=end

