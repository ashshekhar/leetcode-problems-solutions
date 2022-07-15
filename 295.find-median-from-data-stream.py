#
# @lc app=leetcode id=295 lang=python
#
# [295] Find Median from Data Stream
#

# @lc code=start
import heapq

class MedianFinder(object):
  
    def __init__(self):
        
        # Holds the smaller half of the input as a max-heap
        self.small = []
        
        # Holds the bigger half of the input as a min-heap
        self.large = []
        

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        # By default add num to smaller part and then adjust
        heapq.heappush(self.small, -1 * num)
        
        # Make sure the two heaps are sorted
        # Check if the max in smaller half is bigger than least in bigger half
        if (self.small and self.large) and -1 * self.small[0] > self.large[0]:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        # Make sure the length difference between the two heaps are not more than 1
        # Otherwise balance out the heaps
        if len(self.small) - len(self.large) >= 2:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
            
        if len(self.large) - len(self.small) >= 2:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self):
        """
        :rtype: float
        """
        # Same length: Both heaps have same length
        # Take the sum of 2 extremes and divide by 2
        # 123 456 -> 3  + 4 / 2
        if len(self.small) == len(self.large):
            return float(-1 * self.small[0] + self.large[0]) / 2

        # Different lengths: 
        # Return the extreme element from whichever heap has higher num of elements
        # 12 345 -> 3
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        else:
            return self.large[0]
        
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end

