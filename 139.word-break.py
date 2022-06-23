#
# @lc app=leetcode id=139 lang=python
#
# [139] Word Break
#

# @lc code=start
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # dp[i] represents True if there is a sequence starting at ith till i + len(word)th index
        # such that "word" is in wordDict and the remainining portion after the i + len(word)th index
        # is also breakable.
        dp = [False for i in range(len(s) + 1)]
        
        # Base Case
        dp[len(s)] = True
        
        # Loop backwards
        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:
                # If the possible chars starting at ith index are enough to be compared to word
                if (i + len(word)) <= len(s) and s[i : i + len(word)] == word:
                    dp[i] = dp[i + len(word)]

                if dp[i]:
                    break
                
        return dp[0]     
# @lc code=end

