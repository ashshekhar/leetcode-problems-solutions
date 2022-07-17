#
# @lc app=leetcode id=2104 lang=python
#
# [2104] Sum of Subarray Ranges
#

# @lc code=start
class Solution(object):
    def subArrayRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # TC: O(n^2)
        # sum = 0
        
        # for i in range(len(nums)):
        #     maximum = nums[i]
        #     minimum = nums[i]
            
        #     for j in range(i + 1, len(nums)):
        #         maximum = max(maximum, nums[j])
        #         minimum = min(minimum, nums[j])

        #         # Keep updating the sum for each subarray found -> [i ... j]
        #         sum += maximum - minimum
                
        # return sum
    
        # Try in TC: O(n)
        res = 0
        inf = float('inf')
        
        # Finding sum of subarray minimums in negative
        A = [-inf] + nums + [-inf]
        stack = []
        
        for i, x in enumerate(A):
            # Care about the last smaller value
            while stack and A[stack[-1]] > x:
                j = stack.pop()
                k = stack[-1]
                res -= A[j] * (i - j) * (j - k)
            stack.append(i)
        
        # Finding sum of subarray maximums in positive
        A = [inf] + nums + [inf]
        stack = []
        
        for i, x in enumerate(A):
            # Care about the last larger value
            while stack and A[stack[-1]] < x:
                j = stack.pop()
                k = stack[-1]
                res += A[j] * (i - j) * (j - k)
            stack.append(i)
            
        return res
# @lc code=end

