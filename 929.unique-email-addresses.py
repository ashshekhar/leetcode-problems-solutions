#
# @lc app=leetcode id=929 lang=python
#
# [929] Unique Email Addresses
#

# @lc code=start
class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        flag = False
        at = False
        res = ""
        email_set = set()
        
        for em in emails:
            res = ""
            flag = False
            at = False
            
            for char in em:

                if char == ".":
                    if not at:
                        continue

                elif char == "+":
                    flag = True
                    continue
                    
                elif char == "@":
                    at = True
                    flag = False
                    
                elif flag == True:
                    continue
                    
                res += char

            email_set.add(res)
        
        return len(email_set)

# @lc code=end

