#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#

# @lc code=start
from collections import OrderedDict


# Raw approach, using simple dictionary and doubly linked list
# LRUCache: Dictionary will have keys, with values pointing to the correct node of type LRUNode in DLL

class LRUNode():
    def __init__(self, key = 0, val = 0):
        self.key = key
        self.val = val
        self.prev = self.next = None
        
class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.LRUCacheDict = {}
        
        # Creating two LRUNodes to mark the boundaries of DLL structure
        # Initially they point to each other, with no other LRUNodes in between
        self.leftLRU = LRUNode()
        self.rightMRU = LRUNode()
        
        self.leftLRU.next = self.rightMRU
        self.rightMRU.prev = self.leftLRU
    
    def remove_from_DLL(self, node):
        # Connect the prev and next pointers of node
        node.prev.next, node.next.prev = node.next, node.prev
        
    def add_to_right_in_DLL(self, node):
        # Use rightMRU to add
        prev_node, next_node = self.rightMRU.prev, self.rightMRU
        
        prev_node.next, node.next = node, next_node
        next_node.prev, node.prev = node, prev_node
        
        
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.LRUCacheDict:
            # Remove old DLL and add new on right as MRU
            self.remove_from_DLL(self.LRUCacheDict[key])
            self.add_to_right_in_DLL(self.LRUCacheDict[key])
            return self.LRUCacheDict[key].val
              
        return -1
        
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        # Delete if already existing
        if key in self.LRUCacheDict:
            self.remove_from_DLL(self.LRUCacheDict[key])
            del self.LRUCacheDict[key]

        # Add to DLL and LRUCacheDict
        self.new_node = LRUNode(key, value)
        self.LRUCacheDict[key] = self.new_node
        self.add_to_right_in_DLL(self.new_node)
        
        # Check if not exceeding the capacity after insert
        # Otherwise evict the LRU node (left-most) from DLL and LRUCacheDict
        if len(self.LRUCacheDict) > self.capacity:
            to_remove = self.leftLRU.next
            self.remove_from_DLL(to_remove)
            del self.LRUCacheDict[to_remove.key]


# class LRUCache(object):

    # OrderedDict Approach - Simplest, uses move_to_end and popitem(last = False)
    
    # def __init__(self, capacity):
    #     """
    #     :type capacity: int
    #     """
    #     self.capacity = capacity
    #     self.LRUCache = OrderedDict() # Remembers the order of input
        
    # def get(self, key):
    #     """
    #     :type key: int
    #     :rtype: int
    #     """
    #     if key in self.LRUCache.keys():
    #         self.LRUCache.move_to_end(key,last = True)
    #         return self.LRUCache[key]
        
    #     return -1
        
    # def put(self, key, value):
    #     """
    #     :type key: int
    #     :type value: int
    #     :rtype: None
    #     """
    #     self.LRUCache[key] = value
    #     self.LRUCache.move_to_end(key)
        
    #     if(len(self.LRUCache) > self.capacity):
    #         self.LRUCache.popitem(last = False)
    
    
    
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

