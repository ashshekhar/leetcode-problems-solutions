class TicTacToe(object):
  
    def __init__(self, n):
        """
        :type n: int
        """
        self.board = [[None for _ in range(n)] for _ in range(n)]
        self.n = n
    
    # All vals should contain the same playerID else return False
    def checkRowWin(self, row, player):
        for i in range(self.n):
            if self.board[row][i] != player:
                return False
        return True
        
    def checkColWin(self, col, player):
        for i in range(self.n):
            if self.board[i][col] != player:
                return False
        return True
    
    def checkDiagWin(self, player):
        for i in range(self.n):
            if self.board[i][i] != player:
                return False
        return True
        
    def checkAntiDiagWin(self, player):
        for i in range(self.n):
            if self.board[i][self.n - i - 1] != player:
                return False
        return True
    
    def move(self, row, col, player):
        """
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        # Mark the playerId on the board
        self.board[row][col] = player
        
        # Check if the player has won with this move
        # Also check before only, if it is a diagonal or anti diagonal move
        if self.checkRowWin(row, player) or self.checkColWin(col, player) or \
            (row == col and self.checkDiagWin(player)) or \
            (col == self.n - row - 1 and self.checkAntiDiagWin(player)):
                
            return player
    
        return 0
    
# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)