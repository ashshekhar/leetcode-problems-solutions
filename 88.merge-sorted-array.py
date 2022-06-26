#
# @lc app=leetcode id=88 lang=python
#
# [88] Merge Sorted Array
#

# @lc code=start
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        
        # This problem is best done in reverse order because it is guaranteed that there is enough 0s and space
        # m and n represent the number of elements which are yet to be operated on
        last = m + n -1
        
        # Reverse order
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[last] = nums1[m - 1]
                m -= 1
                
            else:
                nums1[last] = nums2[n - 1]
                n -= 1
            
            last -= 1
        
        # Elements left in nums2 - Directly merge until none left
        while n > 0:
            nums1[last] = nums2[n - 1]
            n -= 1
            last -= 1
            
# @lc code=end

