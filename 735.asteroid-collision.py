#
# @lc app=leetcode id=735 lang=python
#
# [735] Asteroid Collision
#

# @lc code=start
import ast
from this import s


class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []

        # Add a while loop, maybe insert an end character
        for i in range(len(asteroids)):
            
            while stack and asteroids[i] < 0 and stack[-1] > 0:
                if abs(asteroids[i]) == abs(stack[-1]):
                    stack.pop()
                    asteroids[i] = 0
                
                elif abs(asteroids[i]) == max(abs(asteroids[i]), abs(stack[-1])):
                    stack.pop()
                
                else:
                    asteroids[i] = 0
            
            if asteroids[i]:      
                stack.append(asteroids[i])
            
        return stack
            
# @lc code=end

