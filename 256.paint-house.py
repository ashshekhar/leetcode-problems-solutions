class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        # Each iteration will update dp for each house
        # dp[j] in ith iteration will represent the min cost to color all houses from 0 to ith house, 
        # where you're coloring the ith house with jth color
        dp = costs[0]
        
        for i in range(1, len(costs)):
            dp0 = costs[i][0] + min(dp[1], dp[2])
            dp1 = costs[i][1] + min(dp[0], dp[2])
            dp2 = costs[i][2] + min(dp[0], dp[1])
            
            dp = [dp0, dp1, dp2]
            
        return min(dp)