#
# @lc app=leetcode id=1395 lang=python
#
# [1395] Count Number of Teams
#

# @lc code=start
class Solution(object):
    def numTeams(self, rating):
        """
        :type rating: List[int]
        :rtype: int
        """
        # Two pointer approach won't work; 
        # Need to use DP
        # Prepare two arrays left and right keeping track of how many numbers are smaller than current in left and right respectively
        # Use this information to find your result

        # lower_dps[i] -> Number of ratings lower than and before ratings[i]
        lower_count = [0 for _ in range(len(rating))]
        
        # upper_dps[i] -> Number of ratings higher than or equal and before ratings[i]
        higher_count = [0 for _ in range(len(rating))]
        
        count = 0
        
        # Get counts
        for i in range(1, len(rating)):
            for j in range(i):
                
                # We found a lower rating before rating[i]
                if rating[j] < rating[i]:
                    lower_count[i] += 1
                    
                # We found a greater or equal rating before rating[i]
                else:
                    higher_count[i] += 1

        # Prepare res
        for i in range(1, len(rating)):
            for j in range(i):
                
                # We found a lower rating before rating[i], check how many more are even lower than rating[j]
                if rating[j] < rating[i]:
                    count += lower_count[j]
                    
                # We found a greater or equal rating before rating[i], check how many are even greater than rating[j]
                else:
                    count += higher_count[j]

        return count
        
# @lc code=end

