#
# @lc app=leetcode id=9 lang=python
#
# [9] Palindrome Number
#

# @lc code=start
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        temp = x
        right_read = 0
        count = 0

        while temp > 0:

            digit = temp % 10
        
            right_read = right_read * 10 + digit
            
            temp = temp / 10

        return x == right_read
        # return str(x) == str(x)[::-1]
# @lc code=end