#
# @lc app=leetcode id=468 lang=python
#
# [468] Validate IP Address
#

# @lc code=start
class Solution:
    def validIPAddress(self, IP):

        def isIPv4(s):
            
            # Check for no leading zeroes and bounds
            # If there are any errors with try, just do except
            try: return str(int(s)) == s and 0 <= int(s) <= 255
            except: return False

        def isIPv6(s):
            
            # Check for bounds and hexadecimal value (int(s, 16) is the hex value of s)
            try: return len(s) <= 4 and int(s, 16) >= 0
            except: return False
        
        if IP.count(".") == 3 and all(isIPv4(i) for i in IP.split(".")):
            return "IPv4"
        
        if IP.count(":") == 7 and all(isIPv6(i) for i in IP.split(":")):
            return "IPv6"
        
        return "Neither"
        
# @lc code=end

