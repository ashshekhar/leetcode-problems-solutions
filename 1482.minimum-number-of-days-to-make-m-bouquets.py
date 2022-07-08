#
# @lc app=leetcode id=1482 lang=python
#
# [1482] Minimum Number of Days to Make m Bouquets
#

# @lc code=start
class Solution(object):
    def minDays(self, bloomDay, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        if m * k > len(bloomDay):
            return -1
        
        def midWorks(mid):
            flowers = 0
            bouquets_needed = m
            
            for bloomDays in bloomDay:
                
                # Count bloomed flowers on mid day
                flowers = flowers + 1 if bloomDays <= mid else 0
                
                # Use to make bouquet if you have enough
                if flowers == k:
                    bouquets_needed -= 1
                    flowers = 0
            
            # Check if the final bouquets_needed are 0 or negative
            return bouquets_needed <= 0
                
            
        # We need to make m bouquets of k adjacent flowers each
        # We will make use of binary search on the number of days
        left = 0
        right = max(bloomDay)

        while left < right:
            mid = left + (right - left) // 2
            
            # Being greedy: If mid works, try to find a smaller number
            if midWorks(mid):
                right = mid
            
            # If it doesn't work, try to find a larger mid day so that more flowers can bloom
            else:
                left = mid + 1
        
        return left
            

# @lc code=end

