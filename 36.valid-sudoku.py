#
# @lc app=leetcode id=36 lang=python
#
# [36] Valid Sudoku
#

# @lc code=start
import collections

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # Use hashmaps with rows and col value as keys and board values as values
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        
        # Key is (i, j)
        squares = collections.defaultdict(set)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    continue
                
                # Check if already present
                if board[i][j] in rows[i] or board[i][j] in cols[j] or board[i][j] in squares[(i // 3, j // 3)]:
                    return False
                
                # Add if not
                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                squares[(i // 3, j // 3)].add(board[i][j])
                
        return True
        
# @lc code=end

