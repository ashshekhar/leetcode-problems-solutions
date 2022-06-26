#
# @lc app=leetcode id=28 lang=python
#
# [28] Implement strStr()
#

# @lc code=start
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not haystack:
            return 0
        
        window_length = len(needle)
        window = ""
        
        for i in range(len(haystack)):
            window = haystack[i : i + window_length]
            
            if window == needle:
                return i
            
        return -1
# @lc code=end

