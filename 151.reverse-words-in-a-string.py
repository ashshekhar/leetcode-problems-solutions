#
# @lc app=leetcode id=151 lang=python
#
# [151] Reverse Words in a String
#

# @lc code=start
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Remove all spaces and create a split array for enumeration using two pointers
        s = " ".join(s.split()).split()

        left = 0
        right = len(s) - 1

        while left <= right:

            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        return " ".join(s)
# @lc code=end

