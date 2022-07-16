#
# @lc app=leetcode id=901 lang=python
#
# [901] Online Stock Span
#

# @lc code=start
class StockSpanner(object):
  
    def __init__(self):
        self.decreasing_stack = []
        

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        res = 1
        
        while self.decreasing_stack and self.decreasing_stack[-1][0] <= price:
            res += self.decreasing_stack.pop()[1]
        
        self.decreasing_stack.append([price, res])
        return res
    
# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
# @lc code=end

