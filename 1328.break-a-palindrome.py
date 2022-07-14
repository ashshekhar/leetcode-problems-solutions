#
# @lc app=leetcode id=1328 lang=python
#
# [1328] Break a Palindrome
#

# @lc code=start
class Solution(object):
    def breakPalindrome(self, palindrome):
        """
        :type palindrome: str
        :rtype: str
        """
        res = ""
        
        if len(palindrome) == 1:
            return res
        
        for i in range(len(palindrome) // 2):
            
            # Replace the first occurence of non-"a" with "a" and return
            if palindrome[i] != "a":
                res = palindrome[:i] + "a" + palindrome[i+1:]
                return res

        # If all were "a" then replace the last char with "b" to keep it lexicographically smallest
        res = palindrome[0:-1] + "b"
        return res
# @lc code=end

