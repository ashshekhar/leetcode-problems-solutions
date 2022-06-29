#
# @lc app=leetcode id=705 lang=python
#
# [705] Design HashSet
#

# @lc code=start
class MyHashSet(object):
  
    # Concept of buckets: Let's choose 10,000 indices, which will hold multiple values based on hash
    def __init__(self):
        self.size = 10000
        
        # Each of these indices will hold a list of values, if hashed key is same
        self.set = [[] for _ in range(self.size)]

    def computeHash(self, index):
        return index % self.size
    
    
    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.map[self.computeHash(key)].append(key)
        
        
    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        index = self.computeHash(key)
        
        if self.map[index]:
            while key in self.map[index]:
                self.map[index].remove(key)
        

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        index = self.computeHash(key)
        
        if self.map[index]:
            return key in self.map[index]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
# @lc code=end

