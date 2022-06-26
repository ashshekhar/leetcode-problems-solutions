#
# @lc app=leetcode id=380 lang=python
#
# [380] Insert Delete GetRandom O(1)
#

# @lc code=start
import random

class RandomizedSet(object):
  
    def __init__(self):
        self.set = {}
        

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.set:
            return False
        else:
            self.set[val] = 1
            
        return True
    
    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.set:
            return False
        else:
            del self.set[val]
        
        return True
    
    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.set.keys())
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end

