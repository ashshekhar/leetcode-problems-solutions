#
# @lc app=leetcode id=419 lang=python
#
# [419] Battleships in a Board
#

# @lc code=start
class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        rows = len(board)
        cols = len(board[0])
        
        count = 0
        
        # Checking vertical, horizontal
        directions = [(1, 0), (0, 1)] 
        
        def dfs(row, col):
            if row < 0 or row >= rows or col < 0 or col >= cols or board[row][col] == ".":
                return

            board[row][col] = "."
            
            for direction in directions:
                dfs(row + direction[0], col + direction[1])
            
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "X":
                    count += 1
                    dfs(i, j)
        
        return count
# @lc code=end

