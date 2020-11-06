class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        initial_x = 0
        initial_y = 0
        
        initial_direction = "N"

        for instruction in instructions:

            if(instruction == "L"):
                if(initial_direction == "N"):
                    initial_direction = "W"
                elif(initial_direction == "W"):
                    initial_direction = "S"
                elif(initial_direction == "E"):
                    initial_direction = "N"
                elif(initial_direction == "S"):
                    initial_direction = "E"
        
            elif(instruction == "R"):
                if(initial_direction == "N"):
                    initial_direction = "E"
                elif(initial_direction == "W"):
                    initial_direction = "N"
                elif(initial_direction == "E"):
                    initial_direction = "S"
                elif(initial_direction == "S"):
                    initial_direction = "W"
                    
            elif(instruction == "G"):
                if(initial_direction == "N"):
                    initial_y += 1
                elif(initial_direction == "W"):
                    initial_x -= 1
                elif(initial_direction == "E"):
                    initial_x += 1
                elif(initial_direction == "S"):
                    initial_y -= 1
            
        if(initial_direction != "N" or (initial_x == 0 and initial_y == 0)):
           return True
        return False