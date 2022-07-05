#
# @lc app=leetcode id=475 lang=python
#
# [475] Heaters
#

# @lc code=start
class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        # Binary Search after sorting
        heaters.sort()
        houses.sort()
        diff = {}
        
        # Initiate the distance with infinity
        for house in houses:
            diff[house] = float("inf")
        
        # For each house, find the nearest heater
        # For each target value, find the nearest number
        for house in houses:
            left = 0
            right = len(heaters)
            
            while left < right:
                mid = left + (right - left) // 2
                
                if heaters[mid] == house:
                    diff[house] = 0
                    break
                
                elif heaters[mid] > house:
                    right = mid
                    diff[house] = min(diff[house], abs(heaters[mid] - house))
                    
                else:
                    left = mid + 1
                    diff[house] = min(diff[house], abs(heaters[mid] - house))

        return max(diff.values())
    
        # Binary Search for the nearest heaters
        
        # Brute Force TLE
        # diff = [float("inf")] * len(houses)
        
        # for heater in heaters:
        #     for i in range(len(houses)):
        #         diff[i] = min(diff[i], abs(heater - houses[i]))
                
        # return max(diff)
                   
# @lc code=end

