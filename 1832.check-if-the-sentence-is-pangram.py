#
# @lc app=leetcode id=1832 lang=python
#
# [1832] Check if the Sentence Is Pangram
#

# @lc code=start
class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        list = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
        
        for alpha in list:
            if alpha not in sentence:
                return False
            
        return True
# @lc code=end

