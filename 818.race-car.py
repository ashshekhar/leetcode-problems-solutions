#
# @lc app=leetcode id=818 lang=python
#
# [818] Race Car
#

# @lc code=start
import collections

class Solution(object):
    def racecar(self, target):
        """
        :type target: int
        :rtype: int
        """
        # Number of moves, current position and velocity
        queue = collections.deque([(0, 0, 1)])
        
        while queue:
            moves, current_pos, current_vel = queue.popleft()
            
            if current_pos == target:
                return moves    
            
            # Accelerate
            queue.append((moves + 1, current_pos + current_vel, current_vel*2))     
            
            # Reverse, considered in 4 cases, get rid of excessive search
            # 2 obvious and 2 foreseeing cases for next step
            if (current_pos > target and current_vel > 0) or (current_pos < target and current_vel < 0) or \
               (current_pos + current_vel > target and current_vel > 0) or (current_pos + current_vel < target and current_vel < 0):
                
                queue.append((moves + 1, current_pos, -1 if current_vel > 0 else 1))
        
        
# @lc code=end

