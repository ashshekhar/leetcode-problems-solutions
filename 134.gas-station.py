#
# @lc app=leetcode id=134 lang=python
#
# [134] Gas Station
#

# @lc code=start
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        # First, the sum of gas >= sum of cost to be able to complete loop
        if sum(gas) < sum(cost):
            return -1
        
        # Now we are guaranteed to complete the loop and one unique solution exists
        # gas -> [1, 2, 3, 4, 5]
        # cost -> [3, 4, 5, 1, 2]
        # diff -> [-2, -2, -2, 3, 3]
        
        diff = 0
        res = 0
        
        for i in range(len(gas)):
            diff += gas[i] - cost[i]
            
            # Kadane's
            # Set res to the next first index
            # in hope that that index will lead to positive diff
            if diff < 0:
                diff = 0
                res = i + 1
        
        return res
                        
# @lc code=end

