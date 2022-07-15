#
# @lc app=leetcode id=516 lang=python
#
# [516] Longest Palindromic Subsequence
#

# @lc code=start
class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        
        n = len(s)
        
        # dp[i][j] represents the length of longest palindromic subsequence between indexes i and j
        dp = [[0] * n for _ in range(n)]
        
        # Bottom up
        for i in range(n - 1, -1, -1):
            
            dp[i][i] = 1
            
            # Cols go from left to right, i + 1 to n - 1
            for j in range(i + 1, n):
                
                # Add 2 and move to two inner values
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                
                # Else max of right or left (disinclude the two non-equals to form 2 smaller subsets)
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return dp[0][n - 1]
        
# @lc code=end

