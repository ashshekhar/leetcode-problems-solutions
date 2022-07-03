#
# @lc app=leetcode id=524 lang=python
#
# [524] Longest Word in Dictionary through Deleting
#

# @lc code=start
class Solution(object):     
    
    # Check if word is a subsequence of s
    def isSubsequence(self, s, word):
        if len(s) < len(word):
            return False
        
        i,j = 0,0
        
        while i < len(s) and j < len(word):
            if s[i] == word[j]:
                i += 1
                j += 1
                
            else:
                i += 1
        
        # Reached the end
        return len(word) == j
        
    def findLongestWord(self, s, dictionary):
        """
        :type s: str
        :type dictionary: List[str]
        :rtype: str
        """
        # Sort by negative length (descending) and lexicographical order
        dic = sorted(dictionary, key = lambda x : (-len(x) , x))

        for word in dic:
            if self.isSubsequence(s, word):
                return word
            
        return  ""
        
# @lc code=end

