#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_dictionary = {}
        t_dictionary = {}
        
        for char in s: 
            if char in s_dictionary:
                s_dictionary[char] += 1
            else:
                s_dictionary[char] = 1
        
        for char in t: 
            if char in t_dictionary:
                t_dictionary[char] += 1
            else:
                t_dictionary[char] = 1
        
        return s_dictionary == t_dictionary
# @lc code=end