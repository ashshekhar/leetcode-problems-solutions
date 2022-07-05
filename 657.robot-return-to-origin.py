#
# @lc app=leetcode id=657 lang=python
#
# [657] Robot Return to Origin
#

# @lc code=start
class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        moves_dict = {"U": (1, 0), "D": (-1, 0), "L": (0, -1), "R": (0, 1)}
        starting_x = 0
        starting_y = 0
        
        for move in moves:
            starting_x += moves_dict[move][0]
            starting_y += moves_dict[move][1]
            
            
        return starting_x == 0 and starting_y == 0
        
# @lc code=end

