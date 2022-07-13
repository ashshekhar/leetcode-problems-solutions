#
# @lc app=leetcode id=937 lang=python
#
# [937] Reorder Data in Log Files
#

# @lc code=start
class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        res = []
        
        for log in logs:
            content = log.split(" ")
            if content[1].isalpha():
                res.append(log)
        
        res = sorted(res, key = lambda x:(x.split(" ")[1: ], x[0]))
        
        for log in logs:
            content = log.split(" ")
            if content[1].isdigit():
                res.append(log)
        
        return res
        
        
# @lc code=end

