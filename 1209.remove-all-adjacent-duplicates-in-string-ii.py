#
# @lc app=leetcode id=1209 lang=python
#
# [1209] Remove All Adjacent Duplicates in String II
#

# @lc code=start
class Solution(object):
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        stack = [] # [char, count]
        
        for i in range(len(s)):
            if stack == [] or stack[-1][0] != s[i]:
                stack.append([s[i], 1])
                
            elif stack[-1][0] == s[i]:
                stack[-1][1] += 1

            if stack[-1][1] == k:
                stack.pop()
        
        string = ""
        for c, v in stack:
            string += c * v
            
        return string
            

# @lc code=end
# "deeedbbcccbdaa" \n 3

