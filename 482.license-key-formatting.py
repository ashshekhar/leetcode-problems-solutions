#
# @lc app=leetcode id=482 lang=python
#
# [482] License Key Formatting
#

# @lc code=start
class Solution(object):
    def licenseKeyFormatting(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
class Solution(object):
    def licenseKeyFormatting(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        res = []
        count = 0

        # Since we need to make sure of k char from reverse
        for _, char in enumerate(s[::-1]):

            if char == "-":
                continue
                
            # Keep appending until allowed
            if count < k:
                res.append(char.upper())
                count += 1
            
            # Count is k, that means need to separate and add this new char in the next part
            elif count == k:
                res.append("-")
                res.append(char.upper())
                count = 1
                
        return "".join(res)[::-1]
            
        
# @lc code=end

