#
# @lc app=leetcode id=402 lang=python
#
# [402] Remove K Digits
#

# @lc code=start
class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        # We are greedy and use increasing monotonic stack to get the smallest number
        # So pop numbers and decrement k whenever you encounter a smaller number
        stack = []
        
        for char in num:
            while stack and stack[-1] > char and k > 0:
                stack.pop()
                k -= 1
            stack.append(char)
        
        # If k was not used up then simply pop k characters
        while k != 0:
            stack.pop()
            k -= 1
            
        res = "".join(stack)  
        
        # Cut leading 0's by converting to int
        # If len(num) == k, then string remaining is empty -> return "0"
        return str(int(res)) if res else "0"
    
# @lc code=end

