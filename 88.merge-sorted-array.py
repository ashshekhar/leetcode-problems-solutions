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
        pointer_1 = 0
        pointer_2 = 0

        while pointer_1 < m and pointer_2 < n and nums1[pointer_1] != 0:

            if(nums1[pointer_1] <= nums2[pointer_2]):
                pointer_1 += 1

            else:
                nums1[pointer_1], nums1[pointer_1 + 1] = nums1[pointer_1 + 1], nums1[pointer_1]
                nums1[pointer_1] = nums2[pointer_2]
                
                pointer_1 += 1
                pointer_2 += 1
        
        while pointer_2 < n:
            if nums1[0] == 0:
                nums1[0] = nums2[0]
            else:
                nums1[pointer_1 + 1] = nums2[pointer_2]
            
            pointer_1 += 1
            pointer_2 += 1
            
        return nums1
# @lc code=end

