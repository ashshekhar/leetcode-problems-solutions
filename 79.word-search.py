#
# @lc app=leetcode id=79 lang=python
#
# [79] Word Search
#

# @lc code=start
class Solution(object):
    def dfs(self, board, word, r, c, row, cols, index):
        if r < 0 or c < 0 or r > row - 1 or c > cols - 1:
            return
        
        char = board[r][c]
        if char != word[index]:
            return 
        
        if index == len(word) - 1 and board[r][c] == word[index]:
            return True
        
        directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        
        board[r][c] = "V"
        
        for direction in directions:
            if self.dfs(board, word, r+direction[0], c+direction[1], row, cols, index+1):
                return True

        # Backtracking
        board[r][c] = char
        
        return False
            
            
            
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        rows = len(board)
        cols = len(board[0])
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    if self.dfs(board, word, i, j, rows, cols, 0):
                        return True
        
        return False
# @lc code=end

