#
# @lc app=leetcode id=1710 lang=python
#
# [1710] Maximum Units on a Truck
#

# @lc code=start
class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        """
        # 1 box of type 1 contains 3 units each - Total 1x3  = 3 units
        # 2 boxes of type 2 contains 2 units each - Total 2x2 = 4 units
        # 3 boxes of type 3 contains 1 unit each - Total 3x1  = 3 units
        # Total allowed boxes = 4 boxes
        # So to maximize units per box, choose max units box first
        
        boxTypes = sorted(boxTypes, key = lambda x:x[1], reverse = True)
        
        count = 0
        res = 0
        i = 0

        while count <= truckSize and i < len(boxTypes):
            
            # Add total units as long as max is not reached
            if count + boxTypes[i][0] <= truckSize:
                count += boxTypes[i][0]
                res += boxTypes[i][0] * boxTypes[i][1]
            
            # Only add as much as allowed
            else:
                temp = count
                count = truckSize
                res += (truckSize - temp) * boxTypes[i][1]
                
            i += 1
            
        return res       
# @lc code=end

