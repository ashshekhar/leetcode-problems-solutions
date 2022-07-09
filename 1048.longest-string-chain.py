#
# @lc app=leetcode id=1048 lang=python
#
# [1048] Longest String Chain
#

# @lc code=start
class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        final = 0
        words = set(words)
        
        # Maps possible word to it's max chain length
        dp = {}
        
        def dfs(word):
            if word in dp:
                return dp[word]
            
            # For the cases, the below loop doesn't run, the result is at least 1
            res = 1
            
            # Generate all words with one char deleted and run DFS
            for j in range(len(word)):
                temp = word[:j] + word[j+1:]
                
                if temp in words:
                    res = max(res, 1 + dfs(temp))
            
            dp[word] = res
            return dp[word]

        # Return the final max of all lengths
        for word in words:
            final = max(final, dfs(word))
            
        return final
        
# @lc code=end

