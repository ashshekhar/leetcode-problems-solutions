#
# @lc app=leetcode id=735 lang=python
#
# [735] Asteroid Collision
#

# @lc code=start
class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []

        # Add a while loop, maybe insert an end character
        for i in range(len(asteroids)):
            
            # Collision 
            while stack and asteroids[i] < 0 and stack[-1] > 0:
                
                # Incoming same as top asteroid
                if abs(asteroids[i]) == abs(stack[-1]):
                    stack.pop()
                    asteroids[i] = 0
                
                # Current incoming asteroid is bigger, smaller explodes
                elif abs(asteroids[i]) == max(abs(asteroids[i]), abs(stack[-1])):
                    stack.pop()
                
                # Else incoming is smaller, it explodes
                else:
                    asteroids[i] = 0
            
            # Only larger incoming gets appended
            if asteroids[i]:      
                stack.append(asteroids[i])
            
        return stack
            
# @lc code=end

