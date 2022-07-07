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
        # Create a 2D Cache DP of m + 1 x n + 1 size
        # cache[i][j] represents the minimum number of operations to convert word1[i:] to word2[j:]
        # Fill the last col and last row as base case
        # Then start filling the 2D DP bottom up as per:
        
            # If the char is equal:
            #    cache[i][j] = cache[i+1][j+1]
            # Else:
            #    cache[i][j] = 1 + min(cache[i][j+1], [i+1][j], [i+1][j+1])
            #    That is,      1 + min(insert, delete, replace)
# @lc code=end

