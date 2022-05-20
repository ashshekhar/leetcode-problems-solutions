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
        # Median is middle element in case of odd, or average of two in even case
        
        l1 = 0
        l2 = 0
        l3 = []
        
        while l1 < len(nums1) and l2 < len(nums2):
            if nums1[l1] < nums2[l2]:
                l3.append(nums1[l1])
                l1 += 1
                
            else:
                l3.append(nums2[l2]) 
                l2 += 1


        while l1 < len(nums1):
            l3.append(nums1[l1])
            l1 += 1
        
        while l2 < len(nums2):
            l3.append(nums2[l2])
            l2 += 1
            
        length = len(l3)
        
        if length % 2 == 0:
            return (Decimal(l3[length // 2]) + Decimal(l3[(length // 2) - 1])) / 2
        else:
            return l3[length // 2] 
# @lc code=end

