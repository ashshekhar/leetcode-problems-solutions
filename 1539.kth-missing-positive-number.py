#
# @lc app=leetcode id=1539 lang=python
#
# [1539] Kth Missing Positive Number
#

# @lc code=start
class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        # Time Complexity: O(N)
        # Space Complexity: O(1)
        
        #  2, 3, 4, 7, 11
        # (k -1 = 4) 1, _, _, _, (Then k - 2 = 2) 5, 6, _, 8, 9 (2 k's used up), ..
        
        # If the kth missing is less than arr[0]
        if k <= arr[0] - 1:
            return k
        
        # Decrease k by the number of positive integers which are missing before the array starts
        k -= arr[0] - 1

        # search kth missing between the array numbers
        for i in range(len(arr) - 1):

            # Number of missing numbers between arr[i] and arr[i + 1]
            curr_missing = arr[i + 1] - arr[i] - 1
            
            # Missing numbers are more than what we have left to allocate
            if k <= curr_missing:
                return arr[i] + k
            
            # Consider using up the positive numbers from the ans set lower than kth
            # Allocating the positive numbers, using them up
            k -= curr_missing

        # If the missing number if greater than arr[-1]
        return arr[-1] + k
        
# @lc code=end

