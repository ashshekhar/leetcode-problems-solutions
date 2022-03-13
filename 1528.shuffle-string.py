#
# @lc app=leetcode id=1528 lang=python3
#
# [1528] Shuffle String
#

# @lc code=start
class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        str = ""
        list_a = list()
        
        list_a = list(zip(s,indices))

        sorted_list = sorted(list_a, key=lambda x: x[1])

        for i in sorted_list:
            str += i[0]
        
        return str
# @lc code=end

