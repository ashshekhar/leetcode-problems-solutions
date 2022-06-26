#
# @lc app=leetcode id=455 lang=python
#
# [455] Assign Cookies
#

# @lc code=start
class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g = sorted(g)
        s = sorted(s)
        
        i = 0
        j = 0
        count = 0
        
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                i += 1
                j += 1
                count += 1
                
            elif g[i] > s[j]:
                j += 1
            
        return count
        
        
# @lc code=end

