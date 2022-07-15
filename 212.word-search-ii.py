#
# @lc app=leetcode id=212 lang=python
#
# [212] Word Search II
#

# @lc code=start

# Still experiencing TLE with last test cases
class TrieNode(object):
    def __init__(self, val = None):
        self.val = val
        self.children = {}
        self.rootword = None
        self.endOfWord = False
        
    def insert(self, word):
        cur = self
        
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode(char)
            cur = cur.children[char]
        
        cur.rootword = word
        cur.endOfWord = True

class Solution(object):
    def dfs(self, row, col, rows, cols, board, node, visit, res):

        if row < 0 or row >= rows or col < 0 or col >= cols or (row, col) in visit \
            or board[row][col] not in node.children:
            return
        
        visit.add((row, col))
        
        node = node.children[board[row][col]]
        
        # If the word is found, append it to the result and mark the end as False to avoid duplicate entries to res
        # For example, ["aa", "aab"], then only once we want "aa"
        if node.endOfWord:
            res.append(node.rootword)
            node.endOfWord = False
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        for direction in directions:
            self.dfs(row + direction[0], col + direction[1], rows, cols, board, node, visit, res)
        
        # Backtracking
        visit.remove((row, col))
        
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        root = TrieNode()
        
        for word in words:
            root.insert(word)
        
        rows = len(board)
        cols = len(board[0])
        visit = set()
        res = []
        
        # Call DFS for each char
        for i in range(rows):
            for j in range(cols):
                self.dfs(i, j, rows, cols, board, root, visit, res)
        
        return res

# @lc code=end

