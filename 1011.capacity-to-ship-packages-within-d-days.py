#
# @lc app=leetcode id=1011 lang=python
#
# [1011] Capacity To Ship Packages Within D Days
#

# @lc code=start
class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        # Idea is to divide the weights into days number of subarrays with minimum sum
        # and return the min sim
        
        # Think of the conveyor belt as ships
        def feasible(capacity):
            
            # (number_of_days = 1) -> One ship is needed min
            number_of_days = 1
            curr_weight = 0
            
            # Start adding linearly onto this first ship
            for w in weights:
                curr_weight += w
                
                # If the weight on the first ship increases cap of each ship
                # Then introduce new ship and start from this last weight which made it heavy
                if curr_weight > capacity:
                    
                    curr_weight = w
                    number_of_days += 1
                    
                    # If by doing so, we exceed the number of ships allowed in total, return False
                    if number_of_days > days:
                        return False
            
            # Else, were successful to ship, so try with a lesser capacity
            return True


        # Min capacity
        left = max(weights)
        
        # Max capacity
        right = sum(weights)
        
        while left < right:
            
            mid = left + (right-left) // 2
        
            # If the number of days we need to ship "mid" is less than the max we have
            # then we need to be more optimal to find the least answer.
            # Therefore, ship lesser per ship, so decrease the avg weight
            if feasible(mid):
                right = mid
            
            # If the number of days we need to ship "mid" is more than what we have, then we need 
            # to ship more per ship, so increase the avg weight
            else:
                left = mid + 1

        return left
# @lc code=end

