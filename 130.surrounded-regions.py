#
# @lc app=leetcode id=130 lang=python
#
# [130] Surrounded Regions
#

# @lc code=start
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        # Capture surrounded regions is same as capturing everything except unsurrounded regions
        # Any region with a part on the border can never be surrounded by 4 sides with X

        rows = len(board)
        cols  = len(board[0])
        visited = set()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        # If out of bounds or not a "O", that is, not a part of border region
        def isValid(row, col):
            return not (row < 0 or row >= rows or col < 0 or col >= cols or (row, col) in visited or board[row][col] != "O")
        
        def dfs(row, col):

            if (row, col) in visited:
                return
            
            board[row][col] = "T"
            visited.add((row, col))
            
            for direction in directions:
                new_r = row + direction[0]
                new_c = col + direction[1]
                
                if isValid(new_r, new_c):
                    board[new_r][new_c] = "T"
                    dfs(new_r, new_c)

        # So we can find unsurrounded regions, mark it "T"
        for i in range(rows):
            if board[i][0] == "O":
                dfs(i, 0)
            if board[i][cols - 1] == "O":
                dfs(i, cols - 1)
        
        for j in range(cols):
            if board[0][j] == "O":
                dfs(0, j)
            if board[rows - 1][j] == "O":
                dfs(rows - 1, j)

        # Capture everything else
        # Mark back the unsurrounded region to original "O"
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "T":
                    board[i][j] = "O"
        
# @lc code=end

