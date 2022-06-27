#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution(object):  
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # This problem demands optimization and hence Greedy algorithm or DP is used
        # dp[i] stores the max profit at each index
        dp = [0 for _ in range(len(prices))]
        
        # Base case
        dp[len(prices) - 1] = 0
        
        for i in reversed(range(len(prices) - 1)):
            profit = (prices[i + 1] - prices[i]) + dp[i + 1]
            
            if profit < 0:
                dp[i] = 0
            else:
                dp[i] = profit
                
        return max(dp)
    
        # Kadane's Algorithm
        # max_so_far = 0
        # final_max = 0
        
        # for i in range(1, len(prices)):
        #     max_so_far += (prices[i] - prices[i-1])

        #     # Better off as empty array
        #     if(max_so_far < 0):
        #         max_so_far = 0 

        #     final_max = max(final_max, max_so_far)
        
        # return final_max 
    
# @lc code=end

