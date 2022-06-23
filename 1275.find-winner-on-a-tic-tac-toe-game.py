#
# @lc app=leetcode id=1275 lang=python
#
# [1275] Find Winner on a Tic Tac Toe Game
#

# @lc code=start
from operator import le


class Solution(object):
    def tictactoe(self, moves):
        """
        :type moves: List[List[int]]
        :rtype: str
        """
        wins = [[[0, 0], [1, 1], [2,2]], [[0, 2], [1, 1], [2, 0]],
                [[0, 0], [1, 0], [2, 0]], [[0, 1], [1, 1], [2, 1]], [[0, 2], [1, 2], [2, 2]], 
                [[0, 0], [0, 1], [0, 2]],[[1, 0], [1, 1], [1, 2]], [[2, 0], [2, 1], [2, 2]]]

        moves_a = []
        moves_b = []
        
        for i in range(len(moves)):
            if i%2 == 0:
                moves_a.append(moves[i])
            else:
                moves_b.append(moves[i])

        for win in wins:
            # all() returns True only if every check corresponds to True inside
            if all(items in moves_a for items in win):
                return "A"
            
            if all(items in moves_b for items in win):
                return "B"
        
        if len(moves) == 9:
            return "Draw"
        
        else:
            return "Pending"
            
        
# @lc code=end

