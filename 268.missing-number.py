#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#

# @lc code=start
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for i in range(0, len(nums)):
            if i not in nums:
                return i
        return i+1
      
# @lc code=end

