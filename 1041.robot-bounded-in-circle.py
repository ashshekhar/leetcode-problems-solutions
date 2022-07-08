#
# @lc app=leetcode id=1041 lang=python
#
# [1041] Robot Bounded In Circle
#

# @lc code=start
class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        # Initial coordinates
        x = 0
        y = 0
        
        # Intially facing north
        direction = 0
        
        # 0 = North, 1 = East, 2 = South, 3 = West
        # On moving G
        possible_moves = {0: [0,1], 1: [1,0], 2: [0,-1], 3: [-1,0]}
        
        # For the math, see how for "L" -> (0 -> 3, 1 -> 0, 2-> 1, 3 -> 2), so +3 % 4
        for instruction in instructions:
            if instruction == 'L':
                direction = (direction + 3) % 4
                
            elif instruction == 'R':
                direction = (direction + 1) % 4
                
            else:
                x = x + possible_moves[direction][0]
                y = y + possible_moves[direction][1]
        
        
        # If after executing the instructions, if you  get your final position at (0,0) 
        # or if you are not facing north direction, that means you will be in circle. 
        
        # Not facing north direction means, as you can repeat the instructions, if you are 
        # not facing north after 1st execution of the instructions, just repeat 3 more times 
        # of the same instructions, you will see yourself at the origin.
        return (direction != 0 or (x == 0 and y == 0))
    

        # Naive approach
        # initial_x = 0
        # initial_y = 0
        
        # initial_direction = "N"

        # for instruction in instructions:

        #     if(instruction == "L"):
        #         if(initial_direction == "N"):
        #             initial_direction = "W"
        #         elif(initial_direction == "W"):
        #             initial_direction = "S"
        #         elif(initial_direction == "E"):
        #             initial_direction = "N"
        #         elif(initial_direction == "S"):
        #             initial_direction = "E"
        
        #     elif(instruction == "R"):
        #         if(initial_direction == "N"):
        #             initial_direction = "E"
        #         elif(initial_direction == "W"):
        #             initial_direction = "N"
        #         elif(initial_direction == "E"):
        #             initial_direction = "S"
        #         elif(initial_direction == "S"):
        #             initial_direction = "W"
                    
        #     elif(instruction == "G"):
        #         if(initial_direction == "N"):
        #             initial_y += 1
        #         elif(initial_direction == "W"):
        #             initial_x -= 1
        #         elif(initial_direction == "E"):
        #             initial_x += 1
        #         elif(initial_direction == "S"):
        #             initial_y -= 1
            
        # if(initial_direction != "N" or (initial_x == 0 and initial_y == 0)):
        #    return True
        # return False
        
# @lc code=end

