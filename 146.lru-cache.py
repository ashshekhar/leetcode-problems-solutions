#
# @lc app=leetcode id=146 lang=python
#
# [146] LRU Cache
#

# @lc code=start
from collections import OrderedDict

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.LRUCache = OrderedDict() # Remembers the order of input
        
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.LRUCache.keys():
            self.LRUCache.move_to_end(key,last = True)
            return self.LRUCache[key]
        
        return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        self.LRUCache[key] = value
        self.LRUCache.move_to_end(key)
        
        if(len(self.LRUCache) > self.capacity):
            self.LRUCache.popitem(last = False)
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

