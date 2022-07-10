class Solution(object):
    def minWindow(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: str
        """       
        rows = len(s1)
        cols = len(s2)
        
        # dp[i][j] holds the starting index in s1 for common sequence between s1[:i+1] and s2[:j+1]
        dp = [[-1 for _ in range(cols + 1)] for _ in range(rows + 1)]
        
        # Base case
        for i in range(rows + 1):
            dp[i][0] = i
            
        length = float('inf')
        res = ""
        
        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                    
                else:
                    dp[i][j] = dp[i-1][j]
                
                # Update result
                if dp[i][cols] != -1 and i - dp[i][cols] < length:
                    length = i - dp[i][cols]
                    res = s1[dp[i][cols] : i]
        return res