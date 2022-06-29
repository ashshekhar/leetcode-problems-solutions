#
# @lc app=leetcode id=52 lang=python
#
# [52] N-Queens II
#

# @lc code=start
class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Appends all unique possible solutions
        res = set()
        
        col_set = set()
        pos_diag_set = set() # (r + c) remains constant
        neg_diag_set = set() # (r - c) remains constant
        
        board = [["."] * n for i in range(n)]
        
        def backtrack(row):
            
            # Let the backtracking take place for the nth row
            # If it was able to place the queen successfully in nth row as well, the row will now be == n
            if row == n:
                res.add(tuple(["".join(row) for row in board]))
                return res 
            
            # For each col in row 1 - Try each column in subsequent rows 
            for col in range(n):
                if col in col_set or (row + col) in pos_diag_set or (row - col) in neg_diag_set:
                    continue
                
                col_set.add(col)
                pos_diag_set.add(row + col)
                neg_diag_set.add(row - col)
                board[row][col] = "Q"
                
                backtrack(row + 1)
            
                # Backtrack       
                col_set.remove(col)
                pos_diag_set.remove(row + col)
                neg_diag_set.remove(row - col)
                board[row][col] = "."
                
        backtrack(0)
        return len(res)
# @lc code=end

