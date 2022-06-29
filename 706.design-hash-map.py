#
# @lc app=leetcode id=706 lang=python
#
# [706] Design HashMap
#

# @lc code=start
class MyHashMap(object):
  
    # Concept of buckets: Let's choose 2069 indices, which will hold multiple (key, value) pairs based on hash
    def __init__(self):
        self.size = 2069
        self.map = [[] for _ in range(self.size)]
    
    
    def computeHash(self, index):
        return index % self.size
    
    
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        index = self.computeHash(key)
        
        if self.map[index]:
            for i, (k, v) in enumerate(self.map[index]):
                if k == key:
                    self.map[index][i] = (key, value)

        else:
            self.map[index].append((key, value))
        
        
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        index = self.computeHash(key)
        res = -1 

        if self.map[index]:
            for i, (k, v) in enumerate(self.map[index]):
                if k == key:
                    res = v
        
        return res

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        index = self.computeHash(key)
        
        if self.map[index]:
            for i, (k, v) in enumerate(self.map[index]):
                if k == key:
                    self.map[index].remove((k, v))

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
# @lc code=end

