#
# @lc app=leetcode id=907 lang=python
#
# [907] Sum of Subarray Minimums
#

# @lc code=start
class Solution(object):
    def sumSubarrayMins(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        # Can't find all combinations using bactracking and then min sumclass Solution(object):

        # arr = [3,1,2,4]
        # List out all subarrays ending with element at index i-> 0 to len(arr)-1
        # result[i] stores the min sum of all subarrays that end in ith element
        
        # result = [0, 3, 2, 4, 8]
        # result[2] = 2 means the minimum sum of all subarrays ending in 2st element in arr = 1
        # All such subarrays -> [3, 1], [1]
        
        arr = [0] + arr
        result = [0] * len(arr)
        stack = [0]
        
        for i in range(len(arr)):
            
            # Find the last smaller value -> We don't care about larger as it won't change the result
            # Keep popping out greater than current element
            while arr[stack[-1]] > arr[i]:
                stack.pop() 
                
            # Last smaller value
            j = stack[-1]
            
            # Reuse the result
            result[i] = result[j] + (i-j) * arr[i]
            
            # Append the index worked with for future indexes
            stack.append(i)
        
        return sum(result) % (10**9+7)
# @lc code=end

