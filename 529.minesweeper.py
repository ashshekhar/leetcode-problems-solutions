#
# @lc app=leetcode id=529 lang=python
#
# [529] Minesweeper
#

# @lc code=start
class Solution(object):
    
    # Return all valid neighbors which are in bounds and yet to be revealed ("M, E")
    def generateValidNeighbors(self, directions, board, row, col, rows, cols):
        res = []
        
        for location in directions:
            if self.checkValidNeighbor(board, location[0] + row, location[1] + col, rows, cols):
                res.append((location[0] + row, location[1] + col))
            
        return res
        
    # There is no use of "X" or "B": Only "M" and "E" are unrevealed
    # So only "M" and "E" in bounds are valid
    def checkValidNeighbor(self, board, row, col, rows, cols):
        if not (row < 0 or row >= rows or col < 0 or col >= cols): 
            if board[row][col] == "E" or board[row][col] == "M":
                return True
            
        return False
                    
            
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        rows = len(board)
        cols  = len(board[0])
        directions = [(-1,-1), (0,-1), (1,-1), (1,0), (1,1), (0,1), (-1,1), (-1,0)]
        
        def dfs(row, col, rows, cols):
            if not self.checkValidNeighbor(board, row, col, rows, cols):
                return
            
            # Mine detected: Change to X
            if board[row][col] == "M":
                board[row][col] = "X"
                return board
            
            # Unrevealed empty square detected
            elif board[row][col] == "E":

                # Find valid neighbors
                neighbors = self.generateValidNeighbors(directions, board, row, col, rows, cols)

                # If neighbors have mines
                mine_count = [board[neighbor[0]][neighbor[1]] for neighbor in neighbors].count("M")

                # Add str digit of how many mines are adjacent to this sqaure
                if mine_count > 0:
                    board[row][col] = str(mine_count)
                    
                # Else change it to B and reveal neighbors recursively
                else:
                    board[row][col] = "B"
                    
                    for valid_neighbors in neighbors:
                        dfs(valid_neighbors[0], valid_neighbors[1], rows, cols)
        
        
        dfs(click[0], click[1], rows, cols)
        return board
        
# @lc code=end

