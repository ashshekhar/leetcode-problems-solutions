#
# @lc app=leetcode id=211 lang=python
#
# [211] Design Add and Search Words Data Structure
#

# @lc code=start
class TrieNode(object):
    def __init__(self, val = None):
        self.val = val
        self.children = {}
        self.endOfWord = False

class WordDictionary(object):

    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        cur = self.root
        
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode(char)
            cur = cur.children[char]
        
        cur.endOfWord = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        node = self.root
        self.res = False
        self.dfs(node, word, 0)
        return self.res

    def dfs(self, node, word, i):
        
        if i >= len(word):
            if node.endOfWord:
                self.res = True
            return
            
        if word[i] == '.':
            # Call DFS for all children of current node
            for n in node.children.values():
                self.dfs(n, word, i + 1)
                
        else:
            # Else move the node to the appropriate child and dfs
            # 'get' since the word[i] could be non-existent in trie
            node = node.children.get(word[i], None)
            if not node:
                return
            self.dfs(node, word, i + 1)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end

