#
# @lc app=leetcode id=338 lang=python
#
# [338] Counting Bits
#

# @lc code=start
class Solution(object):
    # Basic Approach
    # def countOne(self, n):
    #     res = 0
    #     while n:
    #         res += 1 if n&1 else 0
    #         n = n >> 1
        
    #     return res
    
    # def countBits(self, n):
    #     """
    #     :type n: int
    #     :rtype: List[int]
    #     """
    #     result = []

    #     for num in range(0, n+1, 2):
    #         temp = self.countOne(num)
    #         result.append(temp)
            
    #         if n > num:
    #             result.append(temp + 1)
            
    #     return result
            
    # Dynamic Programming Approach
    def countBits(self, n):
        dp = [0] * (n+1)
        
        dp[0] = 0
        if n == 0:
            return dp
        
        dp[1] = 1
        if n == 1:
            return dp
        
        for nums in range(2, n+1):
            if nums % 2 == 0:
                dp[nums] = dp[nums / 2]
            else:
                dp[nums] = dp[nums - 1] + 1

        return dp
        
        
# @lc code=end

