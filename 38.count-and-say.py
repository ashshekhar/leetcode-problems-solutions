#
# @lc app=leetcode id=38 lang=python
#
# [38] Count and Say
#

# @lc code=start
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"
            
        # For i, we need to say i - 1
        to_count = self.countAndSay(n - 1)
        
        # Count and say the returned value
        prev_ptr, current_ptr = 0, 0
        res = ""
        count = 0
        
        while current_ptr < len(to_count):

            while current_ptr < len(to_count) and to_count[current_ptr] == to_count[prev_ptr]:
                count += 1
                current_ptr += 1
            
            res += str(count) + str(to_count[prev_ptr])
            prev_ptr = current_ptr
            count = 0
            
        return res
# @lc code=end

