#
# @lc app=leetcode id=875 lang=python3
#
# [875] Koko Eating Bananas
#

# @lc code=start
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canEat(rate_of_eating):
            hours = 0
            
            for p in piles:
                hours += math.ceil(p / rate_of_eating)
                
                if hours > h:
                    return False
            
            return True

        
        # Decide the min and max rate of eating
        left = 1
        right = max(piles)
        
        while left <= right:
            mid = left + (right - left) // 2

            if canEat(mid):
                right = mid - 1
                
            else:
                left = mid + 1
            
        return left
        
# @lc code=end

