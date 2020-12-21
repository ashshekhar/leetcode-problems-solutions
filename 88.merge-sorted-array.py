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

        nums1_copy = nums1[:m]
        del nums1[:]
        nums1 = []

        pointer_1 = 0
        pointer_2 = 0

        while pointer_1<m and pointer_2<n:

            if(nums1_copy[pointer_1] < nums2[pointer_2]):
                nums1.append(nums1_copy[pointer_1])
                pointer_1 += 1

            else:
                nums1.append(nums2[pointer_2])
                pointer_2 += 1
            
        if pointer_1>=m:
            nums1.extend(nums2[pointer_2:n])

        if pointer_2>=n:
            nums1.extend(nums1_copy[pointer_1:m])
    
        return nums1
# @lc code=end

