#
# @lc app=leetcode id=290 lang=python
#
# [290] Word Pattern
#

# @lc code=start
class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        pat = {}
        strings = s.split(" ")

        if(len(pattern) != len(strings)):
            return False

        for i in range(len(pattern)):
            if pattern[i] not in pat:
                pat[pattern[i]] = [strings[i]]
            else:
                pat[pattern[i]].append(strings[i])
    
        existing_sets = []

        for mapping in pat.values():
            current_set = set(mapping)
            if(current_set in existing_sets):
                return False

            if(len(set(mapping))>1):
                return False
            existing_sets.append(current_set)
            
        return True
# @lc code=end

