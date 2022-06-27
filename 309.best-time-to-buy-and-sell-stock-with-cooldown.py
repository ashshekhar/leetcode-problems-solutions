#
# @lc app=leetcode id=309 lang=python
#
# [309] Best Time to Buy and Sell Stock with Cooldown
#

# @lc code=start
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # Think of the stone game solution
        # Think how you will convert 2^n decision tree to DP and caching
        
        # Keys: (index, is_buying) -> (max_profit)       
        dp = {}
        
        def dfs(index, is_buying):
            if index < 0 or index >= len(prices):
                return 0
            
            if (index, is_buying) in dp:
                return dp[(index, is_buying)]
            
            # In buying state: Two possible options for index state
            if is_buying:
                buy = dfs(index + 1, not is_buying) - prices[index]
                cooldown = dfs(index + 1, is_buying)
                
                dp[(index, is_buying)] = max(buy, cooldown)
            
            # In selling state: Two possible options for index state
            # index + 2 since you need to cooldown for next day after selling
            else:
                sell = dfs(index + 2, not is_buying) + prices[index]
                cooldown = dfs(index + 1, is_buying)
                
                dp[(index, is_buying)] = max(sell, cooldown)
        
            return dp[(index, is_buying)]
        
        return dfs(0, True)
                
# @lc code=end

