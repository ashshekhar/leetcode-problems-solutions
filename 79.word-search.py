#
# @lc app=leetcode id=79 lang=python
#
# [79] Word Search
#

# @lc code=start
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        # Convert 2d matrix to graph adjacency dictionary
        # Use of backtracking
        
        rows, columns = len(board), len(board[0])
        path = set()
        
        # i is the index of the character we are looking for in target word
        def dfs(row, column, i):
            
            if i == len(word):
                return True
            
            if (row < 0 or column < 0 or row >= rows or column >= columns) or (word[i] != board[row][column]) or (row, column) in path:
                return False
            
            # We found our current character
            path.add((row, column))
            
            # Else we found our current char, move on the next character
            result =  dfs(row+1, column, i+1) or dfs(row, column+1, i+1) or dfs(row-1, column, i+1) or dfs(row, column-1, i+1)
            
            path.remove((row, column))
            return result
        
        # Calling the recursive dfs on every cell
        for i in range(rows):
            for j in range(columns):
                if dfs(i, j, 0): return True
        
        return False
# @lc code=end

