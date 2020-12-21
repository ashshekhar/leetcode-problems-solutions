#
# @lc app=leetcode id=66 lang=python
#
# [66] Plus One
#

# @lc code=start
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        num = ""
        output = []
        count = 0
        i = 0

        while(digits[i] == 0):
            count += 1

            if ((i+1) < len(digits)):
                i += 1
            else:
                break

        for i in range(len(digits)):
            num += str(digits[i])

        num = int(num) + 1

        for _ in range(count-1):
            output.append('0')

        for x in str(num):
            output.append(str(x))
            
        return output
        
# @lc code=end

