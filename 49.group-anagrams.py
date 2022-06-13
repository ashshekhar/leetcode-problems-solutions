#
# @lc app=leetcode id=49 lang=python
#
# [49] Group Anagrams
#

# @lc code=start
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        big_dict = {}
        
        for char in strs:
            counter = tuple(sorted(char))

            if counter not in big_dict:
                big_dict[counter] = list()
            
            big_dict[counter].append(char)
        
        return big_dict.values()
            
        
# @lc code=end

