#
# @lc app=leetcode id=1967 lang=python
#
# [1967] Number of Strings That Appear as Substrings in Word
#

# @lc code=start
class Solution(object):
    def numOfStrings(self, patterns, word):
        """
        :type patterns: List[str]
        :type word: str
        :rtype: int
        """
        count = 0
        
        for string in patterns:
            if string in word:
                count += 1
        return count
        
# @lc code=end

