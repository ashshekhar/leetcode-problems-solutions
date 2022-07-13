#
# @lc app=leetcode id=926 lang=python
#
# [926] Flip String to Monotone Increasing
#

# @lc code=start
class Solution(object):
    def minFlipsMonoIncr(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Montone increasing -> Either all 0's, or all 1's or only 0's followed by 1's        
        # For each index, check which is lesser, flipping 1's before the index to 0 or 0's after the index to 1's
        # The index itself doesn't matter as it can be a part of both
        n = len(s)
        ones = 0
        
        zeros = s.count("0")
        
        # Base case -> Flip all zeroes
        minFlips = zeros
        
        for i in range(n):
            if s[i] == "1":
                ones += 1
                
            elif s[i] == "0":
                zeros -= 1

            minFlips = min(minFlips, zeros + ones)
            
        return minFlips
        
        
# @lc code=end

