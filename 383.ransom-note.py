#
# @lc app=leetcode id=383 lang=python
#
# [383] Ransom Note
#

# @lc code=start
from collections import Counter

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ransom = Counter(ransomNote)
        maga = Counter(magazine)
        
        for keys, values in ransom.items():
            if values > maga[keys]:
                return False
            
        return True
# @lc code=end

