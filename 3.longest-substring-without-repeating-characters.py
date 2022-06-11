#
# @lc app=leetcode id=3 lang=python
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        final_max = 0
        current_max = 0
        i = 0
        valid = set()
        left = 0
        
        if s == "":
            return 0
        
        while i < len(s):

            if s[i] not in valid:
                valid.add(s[i])
                current_max += 1
                final_max = max(current_max, final_max)
                
            else:
                while s[i] in valid:
                    valid.remove(s[left])
                    left += 1
                
                valid.add(s[i])
                current_max = len(valid)
                
            i += 1
                
        return final_max
            
            
# @lc code=end

