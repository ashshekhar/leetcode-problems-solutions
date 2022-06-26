#
# @lc app=leetcode id=344 lang=python
#
# [344] Reverse String
#

# @lc code=start
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        left_ptr = 0
        right_ptr = len(s) - 1
        
        while left_ptr <= right_ptr:
            s[left_ptr], s[right_ptr] = s[right_ptr], s[left_ptr]
            
            left_ptr += 1
            right_ptr -= 1
        
        
# @lc code=end

