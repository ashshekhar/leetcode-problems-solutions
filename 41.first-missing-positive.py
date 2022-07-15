#
# @lc app=leetcode id=41 lang=python
#
# [41] First Missing Positive
#

# @lc code=start
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Hard part: TC: O(n) and SC: O(1)
        # So you're only allowed to iterate through nums and not use any additional data structures
        
        # Idea is to understand that ans is between 1 -> len(nums) + 1
        # So any negative or 0 or nums[i] > len(nums) can be marked as 0
        
        # Next, iterate through all nums and change the nums[nums[i] - 1] to += n + 1 if within bounds
        # to mark that when we come back to this index later and find that val plussed by n + 1, 
        # then index + 1 is already present, else index + 1 is my answer
        
        # Worst case, answer is len(nums) + 1
        
        n = len(nums)
        
        # Change all trivial numbers to 0
        for i in range(n):
            if nums[i] < 1 or nums[i] > n:
                nums[i] = 0
                
        # Increment the nums[nums[index] - 1] by n + 1
        # Can be already incremented so mod by n + 1 to go to the correct in-bound index 
        for i in range(n):
            ind = (nums[i] % (n + 1)) - 1
            if 0 <= ind < n:
                nums[ind] += n + 1 
                
        # Check if the number present was incremented by n + 1
        for i in range(n):
            if nums[i] <= n:
                return i + 1
        
        # Worst case
        return n + 1   
    
# @lc code=end

