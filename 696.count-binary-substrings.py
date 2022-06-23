#
# @lc app=leetcode id=696 lang=python
#
# [696] Count Binary Substrings
#

# @lc code=start
class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        
        count = []
        res = 0
        
        left_ptr = 0
        right_ptr = 1
        
        # Prepare the count array using two pointers
        while left_ptr <= right_ptr and right_ptr < len(s):
            
            if s[left_ptr] == s[right_ptr]:
                right_ptr += 1
                
            else:               
                count.append(right_ptr - left_ptr)
                left_ptr = right_ptr
                right_ptr += 1
        
        count.append(right_ptr - left_ptr)

        # Find result using count array
        for i in range(1, len(count)):
            res += min(count[i], count[i-1])
            
        return res
        
# @lc code=end

