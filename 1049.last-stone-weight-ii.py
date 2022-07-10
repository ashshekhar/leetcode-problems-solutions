#
# @lc app=leetcode id=1049 lang=python
#
# [1049] Last Stone Weight II
#

# @lc code=start
class Solution(object):
    def lastStoneWeightII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        # This is dividing the stones in two subsets such that their difference is minimized
        # To minimize the difference, the sum of one subset should reach sum(total) // 2
        # The ans would be the min difference of the two subsets
        
        req = sum(stones)//2        

        # dp[i] stores the closest possible sum to i that can be obtained using the nums in stones
        dp = [0 for i in range(req+1)]
        
        # For each stone
        for stone in stones:
            # For each possible sum from req to equal to greater than num
            for w in range(req, stone-1, -1):
			    
                dp[w] = max(dp[w], stone + dp[w - stone])
                
        # Ans is the difference of subset sums = total - (2 * subset 1 sum)
        return sum(stones) - 2*dp[req]
        
        
# @lc code=end

