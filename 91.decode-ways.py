#
# @lc app=leetcode id=91 lang=python
#
# [91] Decode Ways
#

# @lc code=start
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # dp[i] represents the number of ways to decode an input string of length i
        dp = [0]*(len(s)+1)
        
        # Base Cases
        dp[0] = 1
        dp[1] = 1 if s[0]!='0' else 0 
        
        for i in range(2, len(s)+1):
            if 1 <= int(s[i-1]) <= 9:
                dp[i] += dp[i-1]
                
            if 10 <= int(s[i-2]+ s[i-1]) <= 26:
                dp[i] += dp[i-2]
                
        return dp[len(s)]
    
        # Input: "226"
        # dp: [1, 1, 2, 3]
    
# @lc code=end

