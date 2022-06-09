#
# @lc app=leetcode id=981 lang=python
#
# [981] Time Based Key-Value Store
#

# @lc code=start
from operator import itemgetter

class TimeMap(object):

    def __init__(self):
        self.dictionary = {}
        
        
    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        if key not in self.dictionary:
            self.dictionary[key] = []

        self.dictionary[key].append([value, timestamp])


    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        if key not in self.dictionary:
            return  ""
        
        values = self.dictionary[key]
        
        # Concept of binary search - Assign the most closest valid value to result if in valid condition
        left = 0
        right = len(values) - 1
        result = ""
        
        while left <= right:
            mid = (left + right) // 2
        
            if values[mid][1] == timestamp:
                return values[mid][0]
            
            elif values[mid][1] < timestamp:
                result = values[mid][0]
                left = mid + 1
                
            else:
                right = mid - 1
                
        return result
                
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
# @lc code=end

