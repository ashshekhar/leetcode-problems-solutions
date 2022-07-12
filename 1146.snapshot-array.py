#
# @lc app=leetcode id=1146 lang=python
#
# [1146] Snapshot Array
#

# @lc code=start
import collections

class SnapshotArray(object):
  
    def __init__(self, length):
        """
        :type length: int
        """
        self.snap_id = 0
        
        # Storing snap_id as key in outer dict and val as arrays in the form of dict
        # Inner dictionary is index, val for each array
        self.snap_dict = collections.defaultdict(lambda: collections.defaultdict(int))
        

    def set(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        self.snap_dict[self.snap_id][index] = val

    def snap(self):
        """
        :rtype: int
        """
        # Create a copy with the next snap id
        for indexes in self.snap_dict[self.snap_id]:
            self.snap_dict[self.snap_id + 1][indexes] = self.snap_dict[self.snap_id][indexes]
        
        # Increment the snap counter
        self.snap_id += 1
        
        return self.snap_id - 1

    def get(self, index, snap_id):
        """
        :type index: int
        :type snap_id: int
        :rtype: int
        """
        # print(self.snap_dict)
        return self.snap_dict[snap_id][index]

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
# @lc code=end

