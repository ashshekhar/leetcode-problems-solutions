#
# @lc app=leetcode id=1143 lang=python
#
# [1143] Longest Common Subsequence
#

# @lc code=start
class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        rows = len(text1)
        cols = len(text2)
        
        # Stores the LCS starting from between text1[i:] and text2[j:]
        dp = [[0 for _ in range(cols + 1)] for _ in range(rows + 1)]
        
        # Bottom up with additional row and col
        # Case of moving either along (diagonal) or (right and down)
        for i in range(rows - 1, -1, -1):
            for j in range(cols - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])
                    
        return dp[0][0]
# @lc code=end

