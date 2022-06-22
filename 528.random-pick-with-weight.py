#
# @lc app=leetcode id=528 lang=python
#
# [528] Random Pick with Weight
#

# @lc code=start
import random, bisect

class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.w = w
        
        # Create cumulative sum array
        self.bucket = [0 for _ in range(len(self.w) + 1)]
        
        for i in range(len(self.w)):
            self.bucket[i+1] = self.bucket[i] + self.w[i]
        
        self.bucket = self.bucket[1:]

    def pickIndex(self):
        """
        :rtype: int
        """
        rand = self.bucket[len(self.w) - 1] * random.random()
        
        # Not working
        # rand = random.randint(0, self.bucket[len(self.w) - 1])
        
        # Working built-in Approach
        # return bisect.bisect_left(self.bucket, rand) 
        
        # Other working approach
        for index, cum_sum in enumerate(self.bucket):
            if rand <= cum_sum:
                return index
        
# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
# @lc code=end

