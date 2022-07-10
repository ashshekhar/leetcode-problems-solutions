#
# @lc app=leetcode id=1774 lang=python
#
# [1774] Closest Dessert Cost
#

# @lc code=start
class Solution(object):
    def closestCost(self, baseCosts, toppingCosts, target):
        """
        :type baseCosts: List[int]
        :type toppingCosts: List[int]
        :type target: int
        :rtype: int
        """
class Solution(object):
    def closestCost(self, baseCosts, toppingCosts, target):
        """
        :type baseCosts: List[int]
        :type toppingCosts: List[int]
        :type target: int
        :rtype: int
        """
        toppingCosts = toppingCosts + toppingCosts

        global res
        res = baseCosts[0]
        
        # Return the max cost closest to target
        def backtrack(topping_index, summation):

            global res
            
            # If bigger, then only update if closer to target
            if summation > target:
                if summation - target < abs(target - res):
                    res = summation
                return
            
            # Else keep the smaller one
            if target - summation <= abs(target - res):
                res = summation
            
            if topping_index >= len(toppingCosts):
                return
            
            # Choose current and move to next
            backtrack(topping_index + 1, summation + toppingCosts[topping_index])
            
            # Don't choose and move to next
            backtrack(topping_index + 1, summation)
            
            
        for base in baseCosts:
            backtrack(0, base)
        
        return res
        
# @lc code=end

