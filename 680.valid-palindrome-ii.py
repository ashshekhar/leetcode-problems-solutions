#
# @lc app=leetcode id=680 lang=python
#
# [680] Valid Palindrome II
#

# @lc code=start
class Solution(object):
    def isPalindrome(self, s, i, j):
    
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
                
            else:
                return False
        
        # Odd or even length
        return True
                
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = 0
        right = len(s) - 1
        
        while left < right:
            
            # Should delete one of these
            if s[left] != s[right]:
                return self.isPalindrome(s, left+1, right) or self.isPalindrome(s, left, right-1)
            
            left += 1
            right -= 1
        
        # Original string was palindrome
        return True
        
# @lc code=end

