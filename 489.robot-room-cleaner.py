# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot(object):
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution(object):
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
		# To match robot's turning direction
        # 0, 1, 2, 3 : Up, Right, Down, Left
        directions = [(-1,0), (0,1), (1,0), (0, -1)]
        
        def backtrack(r, c, cur_d, visited):
            robot.clean()
            visited.add((r, c))

            for i in range(4):
                # Here, cur_d refers to - 0, 1, 2, 3 : Up, Right, Down, Left
                new_dir = (cur_d + i) % 4
                
				        # Get neibor's coordinates
                new_r = r + directions[new_dir][0]
                new_c = c + directions[new_dir][1]
                
                if (new_r, new_c) not in visited and robot.move():
                    backtrack(new_r, new_c, new_dir, visited)
                
                # Literally change the robot direction if it can't move to that cell
                # The next for iteration will change the coordinates to this new right
                robot.turnRight()
            
            # There may be some non-cleaned blocks before, so need to clean them
            # Go backward by turning 180 degree
            robot.turnRight()
            robot.turnRight()
            
			      # Going back to previous cell
            robot.move()
            
            # Change back to original direction by turning 180 degree again
            robot.turnRight()
            robot.turnRight()
            
        backtrack(0, 0, 0, set())