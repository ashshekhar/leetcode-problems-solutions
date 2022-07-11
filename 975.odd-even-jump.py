#
# @lc app=leetcode id=975 lang=python
#
# [975] Odd Even Jump
#

# @lc code=start
class Solution(object):
    def oddEvenJumps(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        # Odd jump -> To furthest smaller or equal index
        # Even jump -> To closest greater or equal index
        
        # Even: Closest greater number
        next_higher = [0 for i in arr]
        
        # Odd: Furthest smaller number
        next_smaller = [0 for i in arr]
        
        # Fill in next_higher
        for i in range(len(arr)):
            diff = float("inf")
            for j in range(i + 1, len(arr)):
                if (arr[j] >= arr[i]) and (arr[j] - arr[i] < diff):
                    diff = arr[j] - arr[i]
                    next_higher[i] = j
                
        # Fill in the next_smaller
        for i in range(len(arr)):
            diff = float("inf")
            for j in range(i + 1, len(arr)):
                if (arr[j] <= arr[i]) and (arr[i] - arr[j] < diff):
                    diff = arr[i] - arr[j]
                    next_smaller[i] = j
        
        # Bools for if possible to reach last index with even, odd jumps
        dp = [[False, False] for _ in range(len(arr))]
        
        # Base Case
        dp[len(arr) - 1] = [True, True]
        
        for i in reversed(range(len(arr) - 1)):
            
            # Even jump
            dp[i][0] = dp[next_higher[i]][1]
            
            # Odd jump
            dp[i][1] = dp[next_smaller[i]][0]
        
        # Count of true even jumps
        count = 0
        for i in dp:
            if i[0] == True:
                count +=  1
        return count
        
# @lc code=end

