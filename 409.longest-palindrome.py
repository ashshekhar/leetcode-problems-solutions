#
# @lc app=leetcode id=409 lang=python
#
# [409] Longest Palindrome
#

# @lc code=start
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        dictionary = {}
        result = 0
        
        # To make sure we are only adding 1 odd char even if many are present
        odd = False
        
        for char in s:
            if char not in dictionary:
                dictionary[char] = 1
            else:
                dictionary[char] += 1

        for _, values in dictionary.items():
            if values % 2 == 0:
                result += values
            else:
                # values - 1 ensure if val was 1, 0 is added for now and odd is toggled True
                result += values - 1
                odd = True
        
        if odd:
            return result + 1
        
        return result
            
# @lc code=end

