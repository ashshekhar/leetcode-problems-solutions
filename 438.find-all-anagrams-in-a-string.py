#
# @lc app=leetcode id=438 lang=python
#
# [438] Find All Anagrams in a String
#

# @lc code=start
from collections import Counter

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        length_s = len(s)
        length_p = len(p)
        res = []
        
        dict_p = Counter(p)
        dict_s = Counter()
        
        for i in range(length_s - length_p + 1):
            if not dict_s:
                dict_s = Counter(s[:length_p])
            
            # Instead of making a new Counter, update the old one to save time
            else:
                dict_s[s[i-1]] -= 1
                
                if dict_s[s[i-1]] == 0:
                    del dict_s[s[i-1]]
                    
                dict_s[s[i+length_p-1]] += 1

            if dict_p == dict_s:
                res.append(i)
                
        return res
# @lc code=end

