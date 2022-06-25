#
# @lc app=leetcode id=34 lang=python
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        if not nums or target not in nums:
            return [-1, -1]

        # O(n) is easy to write since it is sorted
        # Write O(log n): Binary Search
        
        def binary_left_index_search(left, right, left_index):
            
            # Base Case
            if left > right:
                return left_index
            
            mid = (left + right) // 2
            
            if nums[mid] == target:
                left_index = mid
                
                # Keep finding a smaller left_index if possible
                return binary_left_index_search(left, mid - 1, left_index)

            elif nums[mid] < target:
                return binary_left_index_search(mid + 1, right, left_index)
                
            else:
                return binary_left_index_search(left, mid - 1, left_index)

        def binary_right_index_search(left, right, right_index):

            # Base Case
            if left > right:
                return right_index
            
            mid = (left + right) // 2
            print(left, right, mid)
            
            if nums[mid] == target:
                right_index = mid
                
                # Keep finding a bigger right_index if possible
                return binary_right_index_search(mid + 1,  right, right_index)

            elif nums[mid] < target:
                return binary_right_index_search(mid + 1, right, right_index)
                
            else:
                return binary_right_index_search(left, mid - 1, right_index)

        left_index = binary_left_index_search(0, len(nums) - 1, -1)
        right_index = binary_right_index_search(0, len(nums) - 1, -1)
        
        return [left_index, right_index]
        
# @lc code=end



