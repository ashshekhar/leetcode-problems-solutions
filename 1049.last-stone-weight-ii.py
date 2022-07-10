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
        
        required_sum = sum(stones)//2        

        # dp[i] stores the closest possible sum to i that can be obtained using the nums in stones
        dp = [0 for i in range(required_sum + 1)]
        
        # For each stone
        for stone in stones:
            
            # For each possible sum from req to equal to greater than num
            for sums in range(required_sum, stone-1, -1):
			    
                dp[sums] = max(dp[sums], stone + dp[sums - stone])
                
        # Ans is the difference of subset sums = total - (2 * subset 1 sum)
        return sum(stones) - 2 * dp[required_sum]
        
        
# @lc code=end

