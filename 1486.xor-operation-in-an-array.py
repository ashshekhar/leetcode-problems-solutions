#
# @lc app=leetcode id=1486 lang=python3
#
# [1486] XOR Operation in an Array
#

# @lc code=start
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        
        nums = [0]*n
        for i in range(n):
            nums[i] = start + 2*i

        XOR = 0

        for i in range(n):
            XOR ^= nums[i]
        
        return XOR
# @lc code=end

