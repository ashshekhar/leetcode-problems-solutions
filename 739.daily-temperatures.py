#
# @lc app=leetcode id=739 lang=python
#
# [739] Daily Temperatures
#

# @lc code=start
class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        decreasing_stack = []
        result = [0] * len(temperatures)

        for current_index, current_temp in enumerate(temperatures):
            
            while decreasing_stack and current_temp > decreasing_stack[-1][1]:
                pop_index = decreasing_stack.pop()[0]
                result[pop_index] = current_index - pop_index
                
            decreasing_stack.append([current_index, current_temp])
        
        return result
        
                
# @lc code=end

