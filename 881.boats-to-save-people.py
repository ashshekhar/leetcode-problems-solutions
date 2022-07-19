#
# @lc app=leetcode id=881 lang=python
#
# [881] Boats to Save People
#

# @lc code=start
class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        
        # Idea is to be greedy, take in the heaviest people first and then
        # try adding a lighter from the other side
        left = 0
        right  = len(people) - 1
        
        res = 0
        remaining_cap = 0
        
        # Left == Right meaning only one person is left
        while left <= right:
            remaining_cap = limit - people[right]
            res += 1
            right -= 1
            
            # Check if a lighter exists and can be added
            if left <= right and people[left] <= remaining_cap:
                left += 1
        
        return res
# @lc code=end

