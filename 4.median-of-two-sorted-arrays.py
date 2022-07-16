#
# @lc app=leetcode id=4 lang=python
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
from decimal import Decimal

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        A = nums1
        B = nums2
        total = len(A) + len(B)
        
        # Make sure A is the smaller one
        if len(A) > len(B):
            A, B = B, A
        
        # Run Binary Search on A and use half to find the nums in B
        # So A[:i+1] and B[:j+1] form the left half of merged arrays
        left = 0
        right = len(A) - 1
        
        # Runs until we return inside
        while True:
            # A
            i = left + (right - left) // 2
            
            # B
            j = (total // 2) - i - 2
            
            # Define the edge values 
            A_left = A[i] if i >= 0 else float("-inf") 
            A_right = A[i + 1] if (i + 1) < len(A) else float("inf")
            
            B_left = B[j] if j >= 0 else float("-inf")
            B_right = B[j + 1] if (j + 1) < len(B) else float("inf")
            
            # Well sorted, return ans
            if A_left <= B_right and B_left <= A_right:
                
                # Total odd
                if total % 2 != 0:
                    return min(A_right, B_right)
                # Total even
                else:
                    return float(max(A_left, B_left) + min(A_right, B_right)) / 2
            
            # Not well sorted - Adjust binary search boundaries
            
            # Need to decrease number of elements in A
            # So move the right pointer, to decrease number of elements
            if A_left > B_right:
                right = i - 1
            
            # Increase number of elements, move the mid forward
            else:
                left = i + 1
                

# @lc code=end

