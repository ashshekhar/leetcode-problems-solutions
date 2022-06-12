#
# @lc app=leetcode id=208 lang=python
#
# [208] Implement Trie (Prefix Tree)
#

# @lc code=start
class TrieNode(object):
    def __init__(self):
        self.next = {}
        self.endNode = False

class Trie(object):

    def __init__(self):
        self.data = TrieNode()
        
    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        current = self.data
        
        for char in word:
            if char not in current.next:
                current.next[char] = TrieNode()
            
            current = current.next[char]
        
        current.endNode = True
            
    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        current = self.data
        
        for char in word:
            if char not in current.next:
                return False
            current = current.next[char]
            
        return current.endNode
            

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        current = self.data
        
        for char in prefix:
            if char not in current.next:
                return False
            current = current.next[char]
        
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end

