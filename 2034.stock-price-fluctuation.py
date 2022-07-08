#
# @lc app=leetcode id=2034 lang=python
#
# [2034] Stock Price Fluctuation 
#

# @lc code=start
import heapq

class StockPrice(object):

    def __init__(self):
        
        # To refer to the latest
        self.timestampToPrice = dict()
        
        # To keep track of max and min prices
        self.min_heap = []
        self.max_heap = []
        
        self.max_time_stamp = 0

    def update(self, timestamp, price):
        """
        :type timestamp: int
        :type price: int
        :rtype: None
        """
        self.max_time_stamp = max(timestamp, self.max_time_stamp)
        
        self.timestampToPrice[timestamp] = price
        heapq.heappush(self.min_heap, (price, timestamp))
        heapq.heappush(self.max_heap, (-price, timestamp))
        
    def current(self):
        """
        :rtype: int
        """
        return self.timestampToPrice[self.max_time_stamp]

    def maximum(self):
        """
        :rtype: int
        """
        # The logic is to return the first pop which matches the correctly updated price in dictionary
        next_max_price, next_time = self.max_heap[0]
            
        while -next_max_price != self.timestampToPrice[next_time] and self.max_heap:
            heapq.heappop(self.max_heap)
            
            next_max_price, next_time = self.max_heap[0]
        
        return -next_max_price

    def minimum(self):
        """
        :rtype: int
        """
        # The logic is to return the first pop which matches the correctly updated price in dictionary
        next_min_price, next_time = self.min_heap[0]
        
        while next_min_price != self.timestampToPrice[next_time] and self.min_heap:
            heapq.heappop(self.min_heap)
            
            next_min_price, next_time = self.min_heap[0]
        
        return next_min_price
    
# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()
# @lc code=end

