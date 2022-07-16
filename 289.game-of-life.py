#
# @lc app=leetcode id=289 lang=python
#
# [289] Game of Life
#

# @lc code=start
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        neighbors = [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]
       
        # Crux of the problem
        # 1 -> 1 if 2 or 3 live neighbors else 1 -> 0
        # 0 -> 1 if 3 live neighbors else  0 -> 0
        
        # Changes based on rules: Original -> New: (Replace original by)
        # 1 -> 1 (2); 1 -> 0 (3); 
        # 0 -> 0 (4); 0 -> 1 (5)
        
        # Valid index
        def isValid(row , col):
            if row >= len(board) or row < 0 or col >= len(board[0]) or col < 0:
                return False
            return True
        
        # Count live neighbors
        def countNeighbors(row, col):
            neighbor = 0
            for (r, c) in neighbors:
                if isValid(row + r, col + c):
                    
                    # Either 1, 2 or 3 represent originally live
                    if board[row + r][col + c] in [1, 2, 3]:
                        neighbor += 1
                    
            return neighbor
        
        # Updating the values based on rules
        for row in range(len(board)):
            for col in range(len(board[0])):
                
                live_neighbors = countNeighbors(row, col)
                
                if board[row][col] == 1:
                    if live_neighbors in [2, 3]:
                        board[row][col] = 2
                    else:
                        board[row][col] = 3
                
                elif board[row][col] == 0:
                    if live_neighbors == 3:
                        board[row][col] = 5
                    else:
                        board[row][col] = 4
        
        # Setting back the correct values             
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == 2 or board[row][col] == 5:
                    board[row][col] = 1
                    
                elif board[row][col] == 3 or board[row][col] == 4:
                    board[row][col] = 0

# @lc code=end

