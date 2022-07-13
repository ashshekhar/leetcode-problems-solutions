#
# @lc app=leetcode id=12 lang=python
#
# [12] Integer to Roman
#

# @lc code=start
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roman_map = [["I", 1], ["IV", 4], ["V", 5], ["IX", 9], ["X", 10], ["XL", 40], ["L", 50], ["XC", 90], ["C", 100], ["CD", 400], ["D", 500], ["CM", 900], ["M", 1000]]
        res = ""
        
        # Go from highest to lowest
        for roman, value in reversed(roman_map):
            
            # Check if the current value is dividing the num or no
            # 2000 -> 2000 // 1000 = 2, so add MM, and reduce the number to 2000 % 2000
            if num // value:
                res += (num // value) * roman
                
                # Next iteration
                num = num % value

        return res            
        
# @lc code=end

