#
# @lc app=leetcode id=125 lang=python
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = ''.join(char for char in s if char.isalnum()).lower()
        
        length = len(s)
        
        if s == "":
            return True
        
        i = 0
        j = length - 1
    
        if length == 2 and s[i] == s[j]:
            return True
          
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
                
            else:
                return False
        
        # Odd or even length
        if i == j or i > j:
            return True
# @lc code=end

