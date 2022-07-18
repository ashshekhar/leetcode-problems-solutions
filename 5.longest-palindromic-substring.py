#
# @lc app=leetcode id=5 lang=python
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Dynamic programming approach
        # Fill half matrix where dp[i, j] = 1 if s[i:j] is a palindrome, 0 otherwise
        # Next, fill the matrix for len >= 3
        # Keep track of max length palindrome while filling the dp table
        
        
        # Expanding around centre approach
        length = len(s)
        
        global res_left, res_right
        res_left, res_right = 0, 0
        
        if length == 1:
            return s[0]
        
        # Expand both ways till the max possible palindrome starting out from index (left, right)
        def expandAroundCentre(left, right):
            
            global res_left, res_right
            while left <= right and right < length and left >= 0 and s[left] == s[right]:
                if right - left >= res_right - res_left:
                    res_right = right
                    res_left = left
                    
                left -= 1
                right += 1     
        
        # Check for both (all odd palindromes) and (all even palindromes)
        # Final answer will be of the length which is bigger out of the two
        for i in range(length):
            
            # If the largest palindrome is odd
            left, right = i, i
            expandAroundCentre(left, right)
            
            # If the largest palindrome is even
            left, right = i,  i + 1
            expandAroundCentre(left, right)
            
        return s[res_left: res_right + 1]
           
# @lc code=end

