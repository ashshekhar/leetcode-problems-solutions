#
# @lc app=leetcode id=647 lang=python
#
# [647] Palindromic Substrings
#

# @lc code=start
class Solution(object):
    def checkPalindrome(self, s, left, right):
        temp_count = 0
        
        while left >= 0 and right < len(s) and s[left] == s[right]:
            temp_count += 1
            left -= 1
            right += 1
            
        return temp_count
            
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # O(n^2) solution
        # The idea is to count all the odd length palindromes and then
        # even length ones, considering the element you are at right now is
        # the middle of a bigger palindromic substring - so you keep moving
        # outward in both directions
        
        count = 0
        
        # Odd length palindromes
        for i in range(len(s)):
            count += self.checkPalindrome(s, i, i)
        
        # Even length palindromes
        for i in range(len(s)):
            count += self.checkPalindrome(s, i, i+1)
        
        return count            

# @lc code=end

