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
        
        i = 0
        j = length - 1
    
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
                
            else:
                return False
        
        return True
# @lc code=end

