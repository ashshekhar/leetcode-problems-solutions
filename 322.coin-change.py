#
# @lc app=leetcode id=322 lang=python
#
# [322] Coin Change
#

# @lc code=start

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # DP Approach
        # dp[i] represents the min coins to get sum i
        dp = [float("inf") for _ in range(amount + 1)]
        
        # Base case
        dp[0] = 0
        
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], 1 + dp[i - coin])
        
        if dp[amount] != float("inf"):
            return dp[amount]
        
        return -1
                
# @lc code=end

