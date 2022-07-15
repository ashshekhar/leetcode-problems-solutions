#
# @lc app=leetcode id=72 lang=python
#
# [72] Edit Distance
#

# @lc code=start
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # cache[i][j] represents the minimum number of operations to 
        # convert word1[i:] to word2[j:]

        # word1 on rows, word2 on columns
        dp = [[float("inf") for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)]
        
        # Base Cases
        for i in range(len(word1) + 1):
            dp[i][len(word2)] = len(word1) - i
        
        for j in range(len(word2) + 1):
            dp[len(word1)][j] = len(word2) - j
        
        
        for i in range(len(word1) - 1, -1, -1):
            for j in range(len(word2) - 1, -1, -1):
                
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                    
                else:
                    # 1 + min(insert, delete, replace)
                    dp[i][j] = 1 + min(dp[i][j + 1], dp[i + 1][j], dp[i + 1][j + 1])
        
        return dp[0][0]
              
# @lc code=end

