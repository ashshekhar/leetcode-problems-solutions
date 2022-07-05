#
# @lc app=leetcode id=179 lang=python
#
# [179] Largest Number
#

# @lc code=start
import functools

class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        # Compare each two integer by converting it to a string value
        # [2, 10] We want to compare 210 > 102 and sort accordingly 
        # such that the values in sorted array should be forming the largest number
        
        def compare(num1, num2):
            if num1 + num2 > num2 + num1:
                # num1 should come first, so return a smaller value that when sorted, will keep the num1 ahead
                return -1
            else:
                return 1
            
        # Covert all values to strings
        for i in range(len(nums)):
            nums[i] = str(nums[i])
        
        # Sort based on the above comparator 
        # Each element calls the above comparator with all other elements
        nums = sorted(nums, key = functools.cmp_to_key(compare))
        
        # Trim out preceeding "0"s
        res =  "".join(nums).lstrip("0")
        
        # If only "0" was the result
        if not res:
            return "0"
        
        return res
    
        
# @lc code=end

